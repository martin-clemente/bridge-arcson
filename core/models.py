from django.db import models

# El contenido institucional se gestiona en core/content.py.
# Si más adelante querés administrar el contenido desde el admin de
# Django (por ejemplo, para que alguien no técnico edite los planes
# o el texto del sitio), estos son buenos puntos de partida:
#
# class Plan(models.Model):
#     nombre = models.CharField(max_length=50)
#     precio = models.DecimalField(max_digits=10, decimal_places=2)
#     destacado = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.nombre
