from django.shortcuts import render
from .models import Project, Task

# Create your views here.
def blog(request):
    projects = Project.objects.all()
    return render(request,'blog.html',{
    'projects':projects
    })

def about(request):
    return render(request,'about.html')