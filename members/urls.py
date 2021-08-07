from members.views import EditUser, PasswordChangedView, PasswordChangingView, UserDashboard, UserLoginView, UserLogoutView, UserRegisterView
from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetView

urlpatterns = [
    path('login', UserLoginView.as_view(), name='login'),
    path('confirm-logout', UserLogoutView.as_view(), name='confirm-logout'),
    path('logged-out', LogoutView.as_view(), name='logout'),
    path('password/', PasswordChangingView.as_view(), name='change_password'),
    path('password_success/', PasswordChangedView.as_view(), name='change_password_done'),
    path('register', UserRegisterView.as_view(), name='register'),
    path('<slug>/dashboard', UserDashboard.as_view(), name='dashboard'),
    path('<username>/edit', EditUser.as_view(), name='edit_user'),
    path('reset_password/', PasswordResetView.as_view(template_name='registration/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', PasswordResetDoneView.as_view(template_name='registration/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_complete'),
    
]