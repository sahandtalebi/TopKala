from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'نام کاربری'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'گذرواژه'})
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if user is None:
            raise forms.ValidationError(" نام کاربری و گذرواژه اشتباه است")

        return self.cleaned_data


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'نام کاربری'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'ایمیل'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'گذرواژه'})
    )
    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'گذرواژه'})
    )

    def clean(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        if password != re_password:
            raise forms.ValidationError("گذرواژه و تکرار گژرواژه با یک دیگر تطابق ندارند")

        user = User.objects.filter(username=username)
        if user:
            raise forms.ValidationError("نام کاربری قبلا استفاده شده است")

        email = User.objects.filter(email=email)
        if email:
            raise forms.ValidationError("ایمیل قبلا استفاده شده است")