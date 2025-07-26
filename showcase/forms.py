from django import forms
from django.contrib.auth.forms import UserCreationForm
from showcase.models import Account, Project
from django.contrib.auth import authenticate


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60)

    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email',
                  'password1', 'password2')


class LoginForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid:
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid Credentials')


class UpdateAccountDetailsForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'profile_pic', 'bio',
                  'skills', 'github_url', 'linkedin_url', 'twitter_url', 'website_url')
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
            'skills': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Python, Django, React, etc.'}),
        }


class UpdateAccountPasswordForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('password1', 'password2')


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('project_name', 'description', 'tech_stack', 'github_link',
                  'live_demo_link', 'google_cloud_link', 'project_image', 'is_featured')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'tech_stack': forms.TextInput(attrs={'placeholder': 'Python, Django, PostgreSQL, etc.'}),
            'github_link': forms.URLInput(attrs={'placeholder': 'https://github.com/...'}),
            'live_demo_link': forms.URLInput(attrs={'placeholder': 'https://...'}),
            'google_cloud_link': forms.URLInput(attrs={'placeholder': 'https://...'}),
        }


class TemplateSelectionForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('portfolio_template',)

        widgets = {
            'portfolio_template': forms.RadioSelect()
        }
