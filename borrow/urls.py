from django.urls import path
from .views import borrow
urlpatterns = [
    path('<int:id>/', borrow, name="borrow"),
]