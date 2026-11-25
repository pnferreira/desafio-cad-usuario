from django.urls import path
from . import views

app_name = "cadastros"
urlpatterns = [
    path("", views.cadastro, name="cadastro"),
    path("sucesso/", views.sucesso, name="sucesso"),
    path("login/", views.entrar, name="login"),
    path("minha-conta/", views.area, name="area"),
    path("sair/", views.sair, name="sair"),
]
