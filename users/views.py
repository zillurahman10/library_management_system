from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login
from .forms import RegistrationForm

# Create your views here.
class UserRegistrationView(FormView):
    template_name = 'user_registration_form.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('homepage')
    
    def form_valid(self,form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)