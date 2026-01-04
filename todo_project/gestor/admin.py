from django.contrib import admin
from .models import Tarea

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'completada', 'importancia', 'usuario', 'fecha_creacion', 'fecha_vencimiento')
    list_filter = ('completada', 'importancia', 'usuario')
    search_fields = ('titulo', 'descripcion', 'usuario__username')
    ordering = ('-fecha_creacion',)
    date_hierarchy = 'fecha_creacion'