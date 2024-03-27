from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"
    def form_valid(self, form):
        # Save the user to the database
        user = form.save()
        # Perform any additional actions here
        # For example, send a welcome email
        return super().form_valid(form)

class LoginView(LoginView):
    success_url = reverse_lazy('home')
    template_name = "registration/login.html"
    # def form_invalid(self, form):
    #     messages.error(self.request, 'Invalid username or password. Please try again.')
    #     return super().form_invalid(form)

class LogoutView(LogoutView):
    # success_url = reverse_lazy('home')
    template_name = "registration/logout.html"