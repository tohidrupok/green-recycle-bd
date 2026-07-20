from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_view(request):

    if request.user.is_authenticated and request.user.is_staff:
        return redirect('dashboard')

    error = None

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            if user.is_staff:

                login(request, user)

                return redirect('dashboard')

            else:

                error = "Access Denied"

        else:

            error = "Invalid Username or Password"

    return render(
        request,
        "panel/login.html",
        {
            "error": error
        }
    )


@login_required(login_url='panel_login')
def dashboard(request):

    if not request.user.is_staff:

        return redirect("panel_login")

    return render(
        request,
        "panel/dashboard.html"
    )


@login_required(login_url='panel_login')
def logout_view(request):

    logout(request)

    return redirect("panel_login")