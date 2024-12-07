from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True, null=True)
    views = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="posts/photos/", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
