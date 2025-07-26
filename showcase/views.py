from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from showcase.forms import RegistrationForm, LoginForm, ProjectForm, UpdateAccountDetailsForm, UpdateAccountPasswordForm, TemplateSelectionForm
from django.contrib.auth.decorators import login_required
from .models import Account, Project
from django.http import HttpResponseRedirect
from django.contrib import messages
import os


'''
home page -
guest users gets option to login or signing up
and after logging in user gets muliple choice of options for creating is Public portfolio
'''
def index(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'devshowcase/index.html', {'user': user})
    else:
        return render(request, 'devshowcase/index.html')


'''
Signup with name, email and password
'''
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
            messages.success(request, 'Registration Successfull')
            return redirect('index')

        else:
            context['registration_form'] = form

    else:
        form = RegistrationForm()
        context['registration_form'] = form

    return render(request, 'devshowcase/registration.html', context)


'''
registered user can login with his email and password
'''
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
    return render(request, 'devshowcase/login.html', context)


'''
logged in user can logout
'''
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Successfully logged out', extra_tags='alert')
    return redirect('index')


'''
user can update or set several set of details
which are not asked at the time of signing up
like profile picture or username
'''


@login_required
def update_account_details(request):
    user = request.user
    if request.method == 'POST':
        form = UpdateAccountDetailsForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save(commit=False)
            if 'profile_pic' in request.FILES:
                user.profile_pic = request.FILES['profile_pic']
            form.save()
            messages.success(request, 'Your details was updated successfully!')
            return redirect('index')

    else:
        form = UpdateAccountDetailsForm(
            initial={
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
            }
        )

    return render(request, 'devshowcase/update_profile.html', {'account_update_form': form})


'''
user can change password
'''


@login_required
def update_account_password(request):
    user = request.user
    if request.method == 'POST':
        form = UpdateAccountPasswordForm(request.POST, instance=request.user)
        if form.is_valid():

            password = form.cleaned_data.get('password1')
            user.set_password(password)
            form.save()
            messages.success(
                request, 'Your password was updated successfully!')
            return redirect('index')

    else:
        form = UpdateAccountPasswordForm()

    return render(request, 'devshowcase/update_password.html', {'password_update_form': form})


'''
functions for performing crud operations
on the user projects
'''

# getting all projects of logged in user
@login_required
def user_projects_list(request):
    user = request.user
    user_projects = Project.objects.filter(account=user)
    return render(request, 'devshowcase/projects.html', {'user_projects': user_projects})

# adding new project to portfolio
@login_required
def add_projects_to_account(request, *args, **kwargs):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.account = request.user
            
            # Create project images directory if it doesn't exist
            project_img_dir = os.path.join('media', 'devshowcase', 'project_images')
            os.makedirs(project_img_dir, exist_ok=True)
            
            project.save()
            messages.success(request, 'Project added successfully!')
            return redirect('showcase:projects')
    else:
        form = ProjectForm()
    
    return render(request, 'devshowcase/add_projects.html', {'form': form})

# deleting existing project
@login_required
def delete_project(request, pk):
    project_to_delete = Project.objects.get(pk=pk)
    project_to_delete.delete()
    messages.success(request, 'Project deleted successfully')
    return HttpResponseRedirect('/projects')


'''
choosing a portfolio template from among the set of given templates,
user portfolio will be rendered in the current chosen template for everyone
if not choosen any template a default template(template 2) is rendered
'''
@login_required
def choose_template(request):
    user = request.user
    form = TemplateSelectionForm()

    if request.POST:
        form = TemplateSelectionForm(request.POST,  instance=request.user)
        form.save()
        return redirect('index')
    return render(request, 'devshowcase/template_selector.html', {'form': form})


'''
publicly accessible portfolio view
anyone with the user's unique portfolio url can view user's portfolio '''
def portfolio(request, pk):
    user = Account.objects.get(pk=pk)
    user_projects = Project.objects.filter(account=user)

    portfolio_template = user.portfolio_template
    
    # Prepare skills list
    skills_list = []
    if user.skills:
        skills_list = [skill.strip() for skill in user.skills.split(',')]
    
    context = {
        'projects': user_projects,
        'account': user,
        'skills_list': skills_list,
    }

    return render(request, 'devshowcase/{}'.format(portfolio_template), context)
