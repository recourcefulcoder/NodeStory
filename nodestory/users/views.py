from django.contrib.auth import login
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import redirect, render

from .forms import RegisterForm


def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            print("VALID", form.cleaned_data)
            user = form.save()
            login(request, user)
            return redirect("homepage:index")
        else:
            print("INVALID")
            print(form.errors)
            for key in form.errors.keys():
                print(f"{key}: {form.errors[key]}")
    else:
        form = RegisterForm()
    return render(request, "users/signup.html", {"form": form})


def review(request):
    if request.user.is_authenticated:
        return render(request, "users/account.html",
                      {"form": UserChangeForm(instance=request.user)})
    return redirect("auth_links:login")
