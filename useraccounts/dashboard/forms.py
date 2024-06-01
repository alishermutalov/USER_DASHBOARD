from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from .models import CustomUser




class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Old password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Old password'}),
       
    )
    new_password1 = forms.CharField(
        label='New password',
        widget=forms.PasswordInput(attrs={'placeholder': 'New password'}),
        
    )
    new_password2 = forms.CharField(
        label='New password confirmation',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm new password'}),
      
    )



class CustomUserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name', 'email', 'phone_number', 'address'] #if you want to allow change photo, you need add 'photo' value in the list
        # Optionally, you can customize the widgets and labels for better form representation
        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'email': forms.EmailInput(),
            'phone_number': forms.TextInput(),
            'address': forms.TextInput(),
        }



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'user1234@example.com'}))
   
    class Meta:
        model = CustomUser
        fields = ('username','email', 'password1', 'password2')
    

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'password'}))
    captcha = CaptchaField()
    
    

