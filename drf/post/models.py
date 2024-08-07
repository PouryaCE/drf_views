from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="post_user")
    title = models.CharField(max_length=50)
    introduction = models.TextField()
    main_pic = models.ImageField()
    category = models.ManyToManyField(Category, verbose_name="post_category")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.user}"





class Image(models.Model):
    image = models.ImageField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="image_post")


class Paragraph(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="paragraph_post")