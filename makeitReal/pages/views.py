from django import forms
from django.shortcuts import render, redirect

from projects.models import Project
from .models import *


from .forms import ContactForm

# Create your views here.


def landing(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("landing")

    form = ContactForm()

    return render(request, "landing.html", context={"form": form})


def index(request):
    projects = Project.objects.filter(available=True).order_by("-id")
    news = News.objects.order_by("-id")
    blogs = Blogs.objects.order_by("-id")

    return render(request, "index.html", {"projects": projects, "blogs": blogs, "news": news})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

    form = ContactForm()
    return render(request, 'contact.html', context={"form": form})


def about(request):
    return render(request, "about.html")
