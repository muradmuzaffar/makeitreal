from django import forms
from django.db import models
from django.forms import fields
from .models import Project


# class AddProject(forms.ModelForm):
#     class Meta:
#         model = Project
#         fields = ['name', 'describtion', 'category', 'image']


class AddProject(forms.ModelForm):
    name = forms.CharField()
    question_1 = forms.CharField()
    question_2 = forms.CharField()
    question_3 = forms.CharField()
    describtion = forms.CharField()
    category = forms.SelectMultiple()
    image = forms.ImageField()

    class Meta:
        model = Project
        fields = ['name', 'question_1', 'question_2',
                  'question_3', 'describtion', 'category', 'image']


class UpdateProject(forms.ModelForm):
    name = forms.CharField()
    question_1 = forms.CharField()
    question_2 = forms.CharField()
    question_3 = forms.CharField()
    describtion = forms.CharField()
    category = forms.SelectMultiple()
    image = forms.ImageField()

    class Meta:
        model = Project
        fields = ['name', 'describtion', 'question_1', 'question_2',
                  'question_3', 'category', 'image']
