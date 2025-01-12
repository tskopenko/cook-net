from django.urls import path

from core.views import (
    index,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    toggle_assign_to_dish,
    CookListView,
    CookDetailView,
    CookCreateView,
    CookDeleteView,
)

app_name = "core"

urlpatterns = [
   path("", index, name='index'),
   path(
        "types/",
        DishTypeListView.as_view(),
        name="type-list",
    ),
   path(
        "types/create/",
        DishTypeCreateView.as_view(),
        name="type-create",
    ),
   path(
        "types/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="type-update",
    ),
   path(
        "types/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="type-delete",
    ),
   path("dishes/", DishListView.as_view(), name="dish-list"),
   path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
   path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
   path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
   path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
   path(
        "dishes/<int:pk>/toggle-assign/",
        toggle_assign_to_dish,
        name="toggle-dish-assign",
    ),
   path("cooks/", CookListView.as_view(), name="cook-list"),
   path(
        "cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"
    ),
   path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
   path(
        "cooks/<int:pk>/delete/",
        CookDeleteView.as_view(),
        name="cook-delete",
    ),
]
