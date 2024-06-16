from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from .forms import RegistrationForm
from . import forms
from django.contrib import messages
from .models import Account
from borrow.models import Borrow
from .models import Account
from books.models import Book
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

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

@login_required(login_url='login')
def deposit_money(request):
    if request.method == 'POST':
        form = forms.DepositForm(request.POST)
        if form.is_valid():
            amount  = form.cleaned_data['balance']
            user = request.user
            account = Account.objects.get(user=user)
            account.balance += amount
            account.save()
            print(user.account.balance)
            messages.success(request, 'Money Deposited Successfully')
            mail_subject = "Deposit Money"
            message = render_to_string('deposit_email.html', {
                'user': request.user.account,
                'amount': amount
            })
            to_email = request.user.email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            return redirect('homepage')
    else:
        form = forms.DepositForm()
    return render(request, 'deposit_money.html', {'form': form})

@login_required(login_url='login')
def profile(request):
    user = request.user
    account = Account.objects.get(user=user)
    data = Borrow.objects.filter(borrower=account)
    print(data)
    return render(request, 'profile.html', {'data': data})

@login_required(login_url='login')
def return_book(request, id):
    if request.method == 'POST':
        user = request.user
        account = Account.objects.get(user=user)
        book = Book.objects.get(id=id)
        borrow = Borrow.objects.get(borrower=account, book=book)
        account.balance += borrow.book.borrowing_price
        account.save()
        borrow.delete()
        messages.success(request, 'You have successfully returned the book')
    return redirect('profile')