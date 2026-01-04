from django.db import models
from django.contrib.auth.models import User

    
class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    completada = models.BooleanField(default=False)
    importancia = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tareas")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.titulo