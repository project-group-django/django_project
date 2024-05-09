from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class UserFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='user_files')
    name = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=50, blank=True)

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.file.name.split('/')[-1]

        ext = self.file.name.split('.')[-1].lower()
        if ext in ['jpg', 'jpeg', 'png', 'gif']:
            self.category = 'image'
        elif ext in ['doc', 'docx', 'txt', 'pdf']:
            self.category = 'document'
        elif ext in ['mp4', 'avi', 'mov']:
            self.category = 'video'
        elif ext in ['mp3', 'wav', 'ogg']:
            self.category = 'audio'
        elif ext in ['zip', 'rar', '7z']:
            self.category = 'archive'
        elif ext in ['exe', 'msi']:
            self.category = 'executable'
        elif ext in ['py', 'java', 'cpp', 'h', 'cs', 'php']:
            self.category = 'programming'
        else:
            self.category = 'other'

        self.category_slug = slugify(self.category)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name