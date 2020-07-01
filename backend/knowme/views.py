from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from knowme.forms import RegistrationForm, LoginForm, ProjectForm
from django.contrib.auth.decorators import login_required
from .models import Account, Project
import imgkit


def index(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        user_projects = Project.objects.filter(account=user)

        for project in user_projects:
            imgkit.from_url(project.google_cloud_link,
                            './media/knowme/project_snaps/{}.jpg'.format(project.project_name))
        return render(request, 'knowme/index.html', {'projects': user_projects})
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
        if form.is_valid:
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


def logout_view(request):
    logout(request)
    return redirect('index')


@ login_required
def add_projects_to_account(request, *args, **kwargs):

    form = ProjectForm()
    if request.POST:
        form = ProjectForm(request.POST)
        if form.is_valid:
            project = form.save(commit=False)
            project.account = request.user
            project.save()

        return redirect('index')

    else:
        form = ProjectForm()
    return render(request, 'knowme/add_projects.html', {'form': form})
