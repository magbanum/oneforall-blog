from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserChangeForm, UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import fields, widgets

class  UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'username', 'placeholder': 'your one-for-all username'}), error_messages={'validation_error': 'Wrong username'})
    password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'your one-for-all password'}))

    class Meta:
        model = User
        fields = ['username', 'password']

    # For desplaying login errors
    def get_invalid_login_error(self):
        if User.objects.filter(username=self.cleaned_data['username']):
            self.non_field_errors = "Password is incorrect." # Can also set field error using self.add_error(field, str)
        else:
            self.non_field_errors = "Username or Password is incorrect."
        return super().get_invalid_login_error()

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self.fields['username'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['password'].widget.attrs.update({'class': 'form-control'})

class PasswordChangingForm(PasswordChangeForm):
    # old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    # new_password1 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    # new_password2 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

class UserChangingForm(UserChangeForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email']

        # def __init__(self, *args, **kwargs):
        #     super(UserChangingForm, self).__init__(*args, **kwargs)

        #     self.fields['username'].widget.attrs.update({'class': 'form-control'})
        #     self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        #     self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        #     self.fields['email'].widget.attrs.update({'class': 'form-control'})