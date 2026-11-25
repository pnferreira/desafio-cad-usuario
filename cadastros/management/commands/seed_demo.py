from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from cadastros.models import Perfil
from django.db import transaction


class Command(BaseCommand):
    help = "Cria uma conta fictícia de referência, sem alterar contas existentes."

    def handle(self, *args, **options):
        with transaction.atomic():
            usuario = User.objects.filter(username="demo@example.com").first()
            if usuario is None:
                usuario = User.objects.create_user(username="demo@example.com", email="demo@example.com", first_name="Alex Demo", password="Sonora2026!")
            Perfil.objects.get_or_create(usuario=usuario, defaults={"idade": 28})
        self.stdout.write("Conta de demonstração disponível: demo@example.com")
