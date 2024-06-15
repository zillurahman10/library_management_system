from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from .forms import RegistrationForm, DepositForm
from . import forms
from django.contrib import messages
from .models import Account

# Create your views here.
class UserRegistrationView(FormView):
    template_name = 'user_registration_form.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('homepage')
    
    def form_valid(self,form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = 'user_login.html'
    def get_success_url(self):
        return reverse_lazy('homepage')
    
class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('homepage')
    
def user_logout(request):
    logout(request)
    return redirect('login')

def deposit_money(request):
    if request.method == 'POST':
        form = forms.DepositForm(request.POST)
        if form.is_valid():
            amount  = form.cleaned_data['balance']
            user = request.user
            account = Account.objects.get(user=user)
            account.balance = account.balance + amount
            account.save()
            print(user.account.balance)
            messages.success(request, 'Money Deposited Successfully')
            return redirect('homepage')
    else:
        form = forms.DepositForm()
    return render(request, 'deposit_money.html', {'form': form})