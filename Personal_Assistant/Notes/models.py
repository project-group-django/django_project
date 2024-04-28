from django.db import models

# Create your models here.

#from django.contrib.auth.models import User


# Create your models here.
class Tag(models.Model):
    tags = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tags}"


class Note(models.Model):
    note = models.CharField(max_length=1500, null=False)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.note}"
