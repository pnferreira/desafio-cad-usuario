from django.contrib.auth.models import User
from django.db import transaction
from .models import Perfil


def criar_conta(dados):
    banco = "legacy"
    with transaction.atomic(using=banco):
        usuario = User.objects.db_manager(banco).create_user(
            username=dados["email"], email=dados["email"],
            first_name=dados["nome"], password=dados["senha"],
        )
        return Perfil.objects.using(banco).create(usuario=usuario, idade=dados["idade"])


def dados_credencial(perfil):
    return {"nome": perfil.usuario.first_name, "codigo": perfil.codigo_credencial}
