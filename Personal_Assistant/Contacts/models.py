from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    birthday = models.DateField()

    def __str__(self):
        return self.name