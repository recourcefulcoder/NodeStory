from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

import users.forms as my_forms


# needs some addition - define handling "invalid form" situation
def signup(request):
    if request.method == "POST":
        form = my_forms.RegisterForm(request.POST)
        if form.is_valid():
            # print("VALID", form.cleaned_data)
            user = form.save()
            login(request, user)
            return redirect("homepage:index")
        # else:
            # print("INVALID")
            # print(form.errors)
            # for key in form.errors.keys():
            #     print(f"{key}: {form.errors[key]}")
    else:
        form = my_forms.RegisterForm()
    return render(request, "users/signup.html", {"form": form})


@login_required
def review(request):
    if request.method == "GET":
        return render(
            request, "users/account_review.html",
        )
    if request.method == "POST":
        # print(request.POST)
        pass


def stories_review(request):
    pass


def password_change(request):
    pass


def username_change(request):
    pass


def email_change(request):
    pass
