from django.shortcuts import render
from books.models import Book, Category

def home(request, category_slug = None):
    data = Book.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        data = Book.objects.filter(categories=category)
    categories = Category.objects.all()
    return render(request, 'index.html', {'data': data, 'categories': categories})