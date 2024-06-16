from django.shortcuts import render, redirect
from .models import Book
from .forms import ReviewForm
from django.contrib import messages
from .models import Review

# Create your views here.
def book_details(request, id):
    data = Book.objects.get(id=id)
    return render(request, 'details.html', {'data': data})

def review_page(request, id):
    form  = ReviewForm(request.POST)
    return render(request, 'review.html', {'form': form, 'id': id})
def review(request, id):
    if request.method == 'POST':
        form  = ReviewForm(request.POST)
        if form.is_valid():
            review = form.cleaned_data['description']
            user = request.user
            book = Book.objects.get(id=id)
            Review.objects.create(user=user,book=book, description=review)
            messages.success(request, 'Review Posted Successfully')
    return redirect('review', id)