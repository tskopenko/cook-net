from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from core.models import Cook, Dish, DishType


def index(request: HttpRequest) -> HttpResponse:
    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()
    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types
    }
    return render(
        request,
        "core/index.html",
        context=context
    )
