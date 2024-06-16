from django.shortcuts import render, redirect
from books.models import Book
from .models import Borrow
from users.models import Account
from django.contrib import messages

# Create your views here.
def borrow(request, id):
    if request.method == "POST":
        book = Book.objects.get(id=id)
        user = request.user
        account = Account.objects.get(user=user)
        if book.borrowing_price > account.balance:
            messages.error(request, 'You do not have sufficient money to borrow :(')
        else:
            account.balance = account.balance - book.borrowing_price
            account.save()
            messages.success(request, 'You have successfully borrowed the book')
        Borrow.objects.create(borrower=account, book=book)
    return redirect('profile')

    