from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.entry_search, name="search"),
    path("new_page", views.entry_new_page, name="new_page"),
    path("wiki/<str:entry>", views.entry_view, name="entry"),
    path("<str:entry>/edit", views.entry_edit, name="edit"),
    path("random_title", views.entry_random, name="random")
]
