from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView, user_logout, deposit_money

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name = "register"),
    path('login/', UserLoginView.as_view(), name = "login"),
    path('logout/', user_logout, name = "logout"),
    path('deposit/', deposit_money, name = "deposit"),
]