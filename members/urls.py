from typing import Pattern
from django import views
from django.urls import path
from django.views.generic.edit import DeleteView
from members.views import PasswordsChangeView, UserLoginView, UserRegisterView, UserEditView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(),name='register'),
    path('edit_profile/', UserEditView.as_view(),name='edit_profile'),
    path('login/', UserLoginView.as_view(), name='log_in'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html')),
    path('password-success/',views.password_success,name='password_success'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_complete'),

]
