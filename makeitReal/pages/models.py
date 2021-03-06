from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.email


class News(models.Model):
    user = models.ForeignKey('auth.User',  on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    describtion = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True)


class Blogs(models.Model):
    user = models.ForeignKey('auth.User',  on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    describtion = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True)
