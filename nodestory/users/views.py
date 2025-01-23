from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

import users.forms as my_forms


def signup(request):
    if request.method == "POST":
        # print(request.POST)
        form = my_forms.RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("homepage:index")
    else:
        form = my_forms.RegisterForm()
    return render(request, "users/signup.html", {"form": form})


@login_required
def review(request):
    if request.method == "GET":
        return render(
            request,
            "users/account_review.html",
        )
    if request.method == "POST":
        # print(request.POST)
        pass


def stories_review(request):
    pass


def username_change(request):
    pass


def email_change(request):
    pass
