from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Curso
from django.template import loader
from app_coder.forms import Curso_formulario
# Create your views here.


def inicio(request):
    
    return render(request, "plantillas.html")


def cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos" : cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render (dicc)
    return HttpResponse ( documento )

def curso_formulario(request):
    
    
    if request.method == "POST":
        
        mi_formulario= Curso_formulario (request.POST)
        
        if mi_formulario.is_valid():
            datos= mi_formulario.cleaned_data
            
        curso = Curso( nombre=datos ['nombre'] , camada=datos ['camada'])
        curso.save()


        return render( request , "formulario.html")

    
    return render(request, "formulario.html")


def buscar_curso(request):
    
    return render( request, "buscar_curso.html")
    
    
def alumnos(request):

    return render(request, "alumnos.html")

def contacto(request):
    
    return render(request, "contacto.html")


def profesores(request):

    return render(request, "profesores.html")


def entregables(request):
    
    return render(request, "entregables.html")

def buscar(request):
    
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        cursos= Curso.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_busqueda.html", {"cursos": cursos})
    else:
        
        return HttpResponse ("Campo vacio")
    
def elimina_curso (request , id):
        
    curso = Curso.objects.get(id=id)
    curso.delete()
    
    curso = Curso.objects.all()
    
    return render(request, "cursos.html", {"cursos" : curso})
        

