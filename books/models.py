from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORIES = [
    ('Sci-Fi', 'Sci-Fi'),
    ('Fantasy', 'Fantasy'),
    ('Horror', 'Horror'),
    ('Romance', 'Romance'),
    ('Mystery', 'Mystery'),
    ('Thriller', 'Thriller'),
    ('Comedy', 'Comedy'),
    ('Action', 'Action'),
    ('Drama', 'Drama'),
    ('Crime', 'Crime'),
    ('Biography', 'Biography'),
    ('History', 'History'),
    ('Health', 'Health'),
    ('Cooking', 'Cooking'),
    ('Education', 'Education'),
    ('Science', 'Science'),
    ('Poetry', 'Poetry'),
    ('Politics', 'Politics'),
    ('Business', 'Business'),
    ('Womens-Fiction', 'Womens-Fiction'),
    ('Religion', 'Religion'),
    ('Spirituality', 'Spirituality'),
    ('Parenting', 'Parenting'),
    ('Travel', 'Travel'),
]

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to = 'books/uploads', blank=True, null=True)
    borrowing_price = models.IntegerField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
    

class Review(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"Commented by {self.user.username} on {self.book.title}"
    

    
