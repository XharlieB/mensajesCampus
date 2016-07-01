from django.db import models

# Create your models here.


class Empleadore(models.Model):
	#atributos
	nombres = models.CharField(max_length=120)
	apellidos = models.CharField(max_length=120)
	edad = models.IntegerField()
	trabajo = models.CharField(max_length=120)
	correo = models.CharField(max_length=120)
	imagen = models.ImageField(upload_to="imagenesPerfilEmpleadores")

	def __str__(self):
		return self.nombres

class Especializacione(models.Model):
	#atributos
	nombre = models.CharField(max_length=120)
	descripcion = models.TextField()

	def __str__(self):
		return self.nombre

class Ubicacione(models.Model):
	#atributos
	calle = models.CharField(max_length=120)
	numero = models.IntegerField()
	colonia = models.CharField(max_length=200)
	delegacionMunicipio = models.CharField(max_length=120)
	tipoLugar = models.CharField(max_length=120)

	def __str__(self):
		return self.calle

class Trabajo(models.Model):
	#atributos
	especializacion = models.ForeignKey(Especializacione, related_name='Especializacion')
	ubicacion = models.ForeignKey(Ubicacione, related_name='Ubicacion')
	#fecha 
	mes = models.CharField(max_length=50)
	hora = models.CharField(max_length=10)
	dia = models.IntegerField()
	pagoHora = models.IntegerField()
	duracionHora = models.IntegerField()

	


