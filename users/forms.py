from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("This email already used")
        return data


class ProfileImageUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [
            'image',
        ]


class ProfileNameUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
        ]


class UserUpdateForm(forms.ModelForm):
    # email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username',
            # 'email',
        ]

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data):
            raise forms.ValidationError("This email already used")
            print('First form error')
        elif User.objects.filter(email=data):
            print("Second Form error")
        else:
            return data
            print('form saved')

    # def clean_email(self):
    #     data = self.cleaned_data['email']
    #     mail = 'user.email'
    #     if not User.objects.filter(email=mail):
    #         return data
    #     else:
    #         raise forms.ValidationError('This email address is already in use.'
    #                                     'Please use a different email address.')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'bio',
        ]


class ProfileImageUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'image',
        ]
