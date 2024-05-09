from django.db import models
from django.contrib.auth.models import User
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    birthday = models.DateField()

    def __str__(self):
        return self.name