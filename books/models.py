from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FileField(upload_to = 'books/uploads')
    borrowing_price = models.IntegerField()

    def __str__(self):
        return self.title
    

class Review(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"Commented by {self.user.username} on {self.book.title}"