from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'homepage'),
    path('user/', include('users.urls')),
    path('book/', include('books.urls')),
    path('category/<slug:category_slug>/', home, name="category_wise_book"),
    path('borrow/', include('borrow.urls')),
]

