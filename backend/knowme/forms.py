from django import forms
from django.contrib.auth.forms import UserCreationForm
from knowme.models import Account, Project
from django.contrib.auth import authenticate


class UpdateAccountForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('first_name', 'last_name',
                  'profile_pic', 'password1', 'password2')


'''
    
'''


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


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('project_name', 'description', 'google_cloud_link')

        widgets = {
            'google_cloud_link': forms.TextInput(attrs={'value': 'https://'}),
        }


class TemplateSelectionForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('portfolio_template',)
