from django.shortcuts import render,redirect
from django.contrib.auth import logout
from app.forms import RegisterForm
from app.models import CardFood


def index(request):
    return render(request, "index.html")

def register(request):
    
    form = RegisterForm()
    context = {"form": form}

    return render(request, "register.html", context)


def logout_view(request):
    logout(request)
    return redirect(index)


def usercab(request):
    request.user
    card_food_list = CardFood.objects.filter(user=request.user).order_by("-pk")
    context = {"card_food_list": card_food_list,
               'page_name': 'ЛК'}
    return render(request, "list.html", context)



def admin_view(request):
    request.user
    card_food_list = CardFood.objects.order_by("-pk")
    context = {"card_food_list": card_food_list,
               'page_name': 'Админпанель'}
    return render(request, "list.html", context)