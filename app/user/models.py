from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=235)
    second_name = models.CharField(max_length=235)
    email = models.EmailField()
    password = models.CharField(max_length=235)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.first_name +  self.second_name}'

    class Meta:
        ordering = ['-email']