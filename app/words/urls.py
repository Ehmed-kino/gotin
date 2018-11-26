from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.get_word, name="get_word"),
    path("<int:word_id>/", views.detail, name="detail"),
]
