from django.contrib.auth.forms import UserChangeForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from members.forms import PasswordChangingForm, RegisterForm, UserChangingForm, UserLoginForm
from django.contrib.auth.views import LoginView, PasswordChangeDoneView, PasswordChangeView
from django.urls import reverse_lazy, reverse
from blog.models import Post
from django.contrib.auth.models import User
# Create your views here.
class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'registration/login.html'

class UserLogoutView(TemplateView):
    template_name = 'registration/confirm_logout.html'

class PasswordChangingView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('change_password_done')

class PasswordChangedView(PasswordChangeDoneView):
    template_name= 'registration/change_password_done.html'
    
class UserRegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserDashboard(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    slug_field = 'username'
    model = Post
    # print(len(queryset))
    template_name = 'registration/dashboard.html'

class EditUser(UpdateView):
    form_class = UserChangingForm
    template_name = 'registration/edit_profile.html'

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse('dashboard', args=[self.object.username])
   