from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('tasks/', views.tasks, name='tasks'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:id>', views.project_detail, name="project_detail"),
    path('autores/', views.autores, name="autores"),
     path('libros/', views.libros, name="libros"), 
     path('autor/<int:id>', views.autor_libros, name="autor_libros"),

]
