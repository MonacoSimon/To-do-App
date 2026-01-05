from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def crear_tarea(request):
    pass

def listar_tareas(request):
    return render(request, 'gestor/base.html')    

def actualizar_tarea(request, tarea_id):
    pass

def eliminar_tarea(request, tarea_id):
    pass

def marcar_como_completada(request, tarea_id):
    pass
   

