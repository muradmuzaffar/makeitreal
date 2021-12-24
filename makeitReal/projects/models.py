from django.db import models
from django.forms.models import ModelChoiceField
from django.shortcuts import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, null=True, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    user = models.ForeignKey('auth.User',  on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    describtion = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True,
                              default="static/images/brand.jpg")
    question_1 = models.CharField(max_length=155, blank=True, null=True,
                                  verbose_name="Why did you come up with this project? What pushed you to thus idea?")

    question_2 = models.CharField(max_length=155, blank=True, null=True,
                                  verbose_name="What is worth of your project? How can it help our society?")

    question_3 = models.CharField(max_length=155, blank=True, null=True,
                                  verbose_name="What is your main goal? How do you see your project in the future(2 years, 5 years)?")

    available = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, null=True)

    def get_absolute_url(self):  # new
        return reverse('profile')

    def __str__(self):
        return self.name


class Comment(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='comments')
    comment_author = models.ForeignKey('auth.User',  on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=140)
