from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    profile_image = models.FileField(upload_to='users/uploads')
    shipping_address = models.CharField(max_length=200)
    balance = models.DecimalField(decimal_places=2, max_digits=12, default=1, blank=True, null=True)

    def __str__(self):
        return self.user.username

