
from django.contrib.auth.views import LoginView, PasswordChangeView
from members.forms import RegisterForm
from django.shortcuts import render
from django.views import generic
from .forms import PasswordChangingForm, RegisterForm, UserChangingForm, UserLoginForm
from django.urls import reverse_lazy


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    # form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request,'registration/password_success.html')

# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = UserChangingForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')

    def password_success(request):
        return render(request,'registration/password_success.html')

    