from django.shortcuts import render


def home_view(request):
    context = {}
    return render(request, "home.html", context)


def login_view(request):
    context = {}
    return render(request, "login_page.html", context)


def buy_view(request):
    context = {}
    print("Hola")
    return render(request, "buy_page.html", context)
