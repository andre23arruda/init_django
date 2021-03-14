from django.db import models

class Book(models.Model):
    registered_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

    def __str__(self):
        return f'{ self.title }'