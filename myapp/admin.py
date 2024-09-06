from django.contrib import admin
from .models import Project, Task, Libro, Autor

# Register your models here.
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Libro)
admin.site.register(Autor)