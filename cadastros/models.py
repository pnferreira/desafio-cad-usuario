from django.conf import settings
from django.db import models
import uuid


class Perfil(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="perfil")
    idade = models.PositiveSmallIntegerField()
    identificador = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    @property
    def codigo_credencial(self):
        return f"SNR-{self.identificador.hex.upper()}"

    def __str__(self):
        return self.usuario.username
