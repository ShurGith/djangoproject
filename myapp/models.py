from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title + ' - ' + self.project.name

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre}  {self.apellidos}"
    
class Libro(models.Model):
    isbn = models.CharField(max_length=13, unique=True)  # ISBN puede tener hasta 13 caracteres
    fecha_publicacion = models.DateField()
    titulo = models.CharField(max_length=200)
    extracto = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    portada = models.CharField(max_length=200,null=True,blank=True,default="https://pic.pnnet.dev/256x256")

    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')

    def __str__(self):
        return self.titulo +' - '+ f"{self.autor.nombre}  {self.autor.apellidos} -  {self.precio}€"