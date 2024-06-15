from django.shortcuts import render
from books.models import Book

def home(request):
    data = Book.objects.all()
    return render(request, 'index.html', {'data': data})