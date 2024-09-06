from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Task, Autor, Libro

# Create your views here.
def index(request):
    return render(request,'index.html')


def blog(request):
    projects = Project.objects.all()
    return render(request,'blog.html',{
    'projects':projects
    })

def about(request):
    return render(request,'about.html')

def projects(request):
    projects = Project.objects.all()
    return render(request,'projects.html',{
    'projects':projects
    })

def tasks(request):
    tasks = Task.objects.all()
    return render(request,'tasks.html',{
    'tasks':tasks
    })

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })


def autores(request):
    autores = Autor.objects.all()
    return render(request,'autores.html',{
    'autores':autores
    })

def autor_libros(request, id):
    autor = get_object_or_404(Autor, id=id)
    libros = Libro.objects.filter(autor_id=id)
    return render(request, 'autor_libros.html', {
        'autor': autor,
        'libros': libros
    })
def libros(request):
    libros = Libro.objects.all()
    return render(request,'libros.html',{
    'libros':libros
    })