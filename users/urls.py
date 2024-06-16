from django.urls import path
from .views import UserRegistrationView, UserLoginView, profile, user_logout, deposit_money, return_book

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name = "register"),
    path('login/', UserLoginView.as_view(), name = "login"),
    path('profile/', profile, name = "profile"),
    path('logout/', user_logout, name = "logout"),
    path('deposit/', deposit_money, name = "deposit"),
    path('return_book/<int:id>', return_book, name = "return_book"),
]