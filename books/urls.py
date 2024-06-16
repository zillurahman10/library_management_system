from django.urls import path
from .views import book_details, review, review_page

urlpatterns = [
    path('details/<int:id>', book_details, name="details"),
    path('review/<int:id>', review_page, name="review"),
    path('post_review/<int:id>', review, name="post_review"),
]