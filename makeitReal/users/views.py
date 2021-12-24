from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from projects.models import Project
from django.contrib.auth.forms import UserCreationForm


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def user_register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=password)
            # login(request, user)

            return redirect("index")

        else:
            form = NewUserForm()
            return render(request=request, template_name="register.html", context={"register_form": form})

    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def user_logout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("landing")


def profile(request):
    projects = Project.objects.filter(user=request.user)
    # messages.error(request , 'There is no Project. Click the Add Project button to add the Project')
    return render(request, 'profile.html', {'projects': projects})
