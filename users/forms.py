from django import forms
from django.forms import ModelForm
from .models import User,Profiles

class Login_Register_Form(ModelForm):
    class Meta:
        model = User
        fields=['username', 'password',]

        widgets={
            'username':forms.TextInput(attrs={'class':'login-username'}),
            'password':forms.PasswordInput(attrs={'class':'login-password'}),
        }

        labels={
            'username':('Your Username'),
            'password':('Your Password'),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user



class User_Profile_Register_Form(ModelForm):
    class Meta:
        model=Profiles
        exclude=['created_time','connected']

        widgets={
            'user_avatar':forms.FileInput(attrs={'class':'user-avatar-edit'}),
            'user_signature':forms.TextInput(attrs={'class':'user-signature-edit'}),
        }


        labels={
            'user_avatar': ('Your Avatar'),
            'user_signature':('Your Signature'),
        }