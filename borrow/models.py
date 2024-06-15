from django.db import models
from users.models import Account
from books.models import Book

# Create your models here.
class Borrow(models.Model):
    borrower = models.ForeignKey(Account, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)