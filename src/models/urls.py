from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get-word", views.get_word, name="api-get-word"),
]
