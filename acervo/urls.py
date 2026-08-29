from django.urls import path

from acervo import views

urlpatterns = [
    path("autores/", views.autor_list, name="autor_list"),
    path("autores/<int:pk>/", views.autor_detail, name="autor_detail"),
]
