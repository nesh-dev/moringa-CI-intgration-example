from django.db import models
from user.models import Author

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=235)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
        
class Blog(models.Model):
    title = models.CharField(max_length=235)
    description = models.CharField(max_length=235)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return self.title





