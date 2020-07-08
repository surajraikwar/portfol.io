from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from knowme.forms import RegistrationForm, LoginForm, ProjectForm, UpdateAccountForm, TemplateSelectionForm
from django.contrib.auth.decorators import login_required
from .models import Account, Project
import imgkit


def index(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        #user_projects = Project.objects.filter(account=user)
        return render(request, 'knowme/index.html', {'pk': user.pk})
    else:
        return render(request, 'knowme/index.html')


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')

            account = authenticate(email=email, password=password)
            login(request, account)
            return redirect('index')

        else:
            context['registration_form'] = form

    else:
        form = RegistrationForm()
        context['registration_form'] = form

    return render(request, 'knowme/registration.html', context)


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('index')
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('index')

    else:
        form = LoginForm()
    context['login_form'] = form
    return render(request, 'knowme/login.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('index')


def portfolio(request, pk):
    #user = get_object_or_404(Account, pk=pk)
    user = Account.objects.get(pk=pk)
    user_projects = Project.objects.filter(account=user)

    #user = request.user

    portfolio_template = user.portfolio_template

    return render(request, 'knowme/{}'.format(portfolio_template), {'projects': user_projects, 'account': user})
    # if user.is_authenticated:
    #user_projects = Project.objects.filter(account=user)
    # return render(request, 'knowme/{}'.format(portfolio_template), {'projects': user_projects, 'account': user})


@login_required
def update_account_details(request):
    user = request.user
    if request.method == 'POST':
        form = UpdateAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save(commit=False)
            if 'profile_pic' in request.FILES:
                user.profile_pic = request.FILES['profile_pic']
            password = form.cleaned_data.get('password1')
            user.set_password(password)
            form.save()
            #update_session_auth_hash(request, user)
            return redirect('index')

    else:
        form = UpdateAccountForm(
            initial={
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
            }
        )

    return render(request, 'knowme/update_profile.html', {'account_update_form': form})


'''


'''


@login_required
def add_projects_to_account(request, *args, **kwargs):

    form = ProjectForm()
    options = {'crop-h': '700', 'quiet': ''}
    if request.POST:
        form = ProjectForm(request.POST)
        if form.is_valid:
            project = form.save(commit=False)
            imgkit.from_url(project.google_cloud_link,
                            './media/knowme/project_snaps/{}.jpg'.format(project.project_name), options=options)
            project.account = request.user
            project.save()

        return redirect('index')

    else:
        form = ProjectForm()
    return render(request, 'knowme/add_projects.html', {'form': form})


@login_required
def choose_template(request):
    user = request.user
    form = TemplateSelectionForm()

    if request.POST:
        form = TemplateSelectionForm(request.POST,  instance=request.user)
        form.save()
        return redirect('index')
    return render(request, 'knowme/template_selector.html', {'form': form})
