from django import forms
from .models import Task
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'complete')

        labels = {
            'title': "",
            'description': "",
            'complete': "completed?"
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'h-16 text-2xl mt-5 mb-2 bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder': 'Task Title'}),
            'description': forms.TextInput(attrs={'class': 'h-16 text-2xl mt-5 mb-2 bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder': 'Description'}),
            'complete': forms.CheckboxInput(attrs={'class': 'form-check-input appearance-none h-4 w-4 border border-gray-300 rounded-sm bg-white checked:bg-blue-600 checked:border-blue-600 focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain float-left mr-2 cursor-pointer" type="checkbox" value="" id="flexCheckChecked" checked'}),
        }

class UserLoginForm(AuthenticationForm):
        username = forms.CharField(label="", max_length=254,widget=forms.TextInput(attrs={'class': 'h-16 text-2xl mt-5 mb-2 bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder': 'Username'}),)
        password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'h-16 text-2xl mt-5 mb-2 bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder': 'Password'}))


class TaskUpdate(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'complete')

        labels = {
            'title': "",
            'description': "",
            'complete': "completed?"
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'h-16 text-2xl mt-5 mb-2 bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder': 'Task Title'}),
            'description': forms.Textarea(attrs={'class': 'h-40 text-2xl mt-5 mb-2 bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder': 'Description'}),
            'complete': forms.CheckboxInput(attrs={'class': 'form-check-input appearance-none h-4 w-4 border border-gray-300 rounded-sm bg-white checked:bg-blue-600 checked:border-blue-600 focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain float-left mr-2 cursor-pointer" type="checkbox" value="" id="flexCheckChecked" checked'}),
        }

class UserCreationForm(UserCreationForm):
        username = forms.CharField(label='', min_length=4, max_length=150, widget=forms.TextInput(attrs={'class': 'h-16 text-2xl mt-5 mb-2 bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder': 'Username'}))
        password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'h-16 text-2xl mt-5 mb-2 bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder': 'Password'}))
        password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'h-16 text-2xl mt-5 mb-2 bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder': 'Confirm Password'}))
        
        
        def clean_username(self):
            username = self.cleaned_data['username'].lower()
            r = User.objects.filter(username=username)
            if r.count():
                raise  ValidationError("Username already exists")
            return username

        def clean_password2(self):
            password1 = self.cleaned_data.get('password1')
            password2 = self.cleaned_data.get('password2')

            if password1 and password2 and password1 != password2:
                raise ValidationError("Password don't match")

            return password2

        def save(self, commit=True):
            user = User.objects.create_user(
                self.cleaned_data['username'],
                self.cleaned_data['password1']
            )
            return user