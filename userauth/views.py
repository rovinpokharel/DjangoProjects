from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm,CustomUserUpdateForm
from django.views.generic import DetailView, UpdateView
from .models import CustomUser
from django.urls import reverse_lazy

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'userauth/signup.html'
    def get_success_url(self):
        return reverse_lazy('userauth:login')
        # reverse lazy le main project ko url ko namespace ko urls use garcha
        # return '/restaurant/'

class UserLoginView(LoginView):
    template_name = 'userauth/login.html'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('restaurants:list')
        # return '/restaurant/'

class UserProfileView(LoginRequiredMixin,DetailView):
    # LoginRequiredMixin le kei page kholnu agadi login garna parcha bhancha
    login_url = reverse_lazy('userauth:login')
    template_name = "userauth/profile.html"
    def get_object(self, queryset=None):
        username = self.request.user.get_username()
        user_detail = get_object_or_404(CustomUser, username = username)
        return user_detail

class UserProfileUpdateView(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('userauth:login')
    form_class = CustomUserUpdateForm
    template_name = "userauth/update.html"

    def get_object(self, queryset=None):
        username = self.request.user.get_username()
        user_detail = get_object_or_404(CustomUser, username = username)
        return user_detail

    def get_success_url(self):
        return reverse_lazy('userauth:profile')
        # return '/user-profile/'