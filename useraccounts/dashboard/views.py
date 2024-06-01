from django.urls import reverse_lazy 
from django.views.generic import ListView, UpdateView , CreateView
from .forms import CustomPasswordChangeForm, CustomUserUpdateForm, UserRegisterForm, UserLoginForm
from .models import CustomUser, Followers
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.shortcuts import redirect, render
# Create your views here.


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class UserAccountListView(ListView):
    model = CustomUser
    context_object_name = 'user'
    template_name = 'dashboard/customuser_list.html'
    def get_queryset(self):
        user_id = self.request.user.pk
    # Filter the queryset to include only objects related to the user
        try:
            queryset = super().get_queryset().get(pk=user_id)
            return queryset
        except Exception as e:
            return HttpResponse(str(e))
        
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["title"] = "My account"
        return context
    
        

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CustomUserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = 'dashboard/account_update.html'
    success_url = reverse_lazy('profile')
    context_object_name = 'user'
    def get_object(self):
        return self.request.user
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit account"
        return context
    

class RegisterView(CreateView):
    form_class = UserRegisterForm 
    template_name = 'dashboard/register.html' # v01 is app name
    success_url = reverse_lazy('login') # if form is valid, user will redirect to login page
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Register'
        return context


class CustomLoginView(LoginView):
    form_class = UserLoginForm # Custom login form
    template_name = 'dashboard/login.html' # v01 is app name
    # success_url = reverse_lazy('home')
    
    
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            messages.success(self.request, 'Login successful!')
            return redirect('profile')
        else:
            messages.error(self.request, 'Invalid username or password')
            return self.form_invalid(form)
    
    # Optionally add extra context or override methods.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context
    
    
def user_logout(request): #logout view
    logout(request)
    return redirect('login') #after logging out, redirect to login page


class HomeView(ListView):
    model = CustomUser
    template_name = 'dashboard/home.html'
    context_object_name='users'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home"
        return context

class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'dashboard/change_password.html'
    success_url = reverse_lazy('password_change_done')
    
def password_change_done(request):
    return render(request,'dashboard/password_change_done.html')