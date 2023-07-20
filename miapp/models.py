from django.db import models

# Create your models here.

class Article(models.Model):
    title= models.CharField(max_length=150, verbose_name="Titulo") #charfield es tipo de dato texto
    content= models.TextField()#T.D cuadro grande
    image= models.ImageField(default='null', upload_to='articles') #Agregar una imagen y debe poner una ruta
    public= models.BooleanField() #Verdadero o falso
    created_at= models.DateTimeField(auto_now_add=True) #Guarda la fecha al momento de la creacion
    updated_at= models.DateTimeField(auto_now=True) #guarda cuando se modifica

    class Meta:
        verbose_name="Articulo" #nombre que quiero q se llame la clase/ TAmbien sirve para cambiar nombre a atributos
        verbose_name_plural="Articulos" # pluralizado
        ordering = ['id'] # con el - delante se hace invertido solo en mod.Adm
    
    def __str__(self): # esto es para ver que mostrar en el menu adm
        if self.public:
            publico="Publicado"
        else:
            publico="No Publicado"
        return f"{self.title} ** Estado: {publico} **"

class Category(models.Model):
    name= models.CharField(max_length=110)
    description=models.CharField(max_length=250)
    created_at=models.DateField() #Fecha manual

    class Meta:
        verbose_name="Categoria" #nombre que quiero q se llame la clase
        verbose_name_plural="Categorias" # pluralizado

#Crear Tablas, en cmd se ejecuta
# 1.- se crea Migracion ** python manage.py makemigrations (crea arch en migrations)
# 2.- Crear el SQL ese archivo creado ** python manage.py sqlmigrate miapp 0001 (nombre de app y numero de migracion)
# 3.- Ejecutar el comando N° 2 con ** python manage.py migrate (queda ok las tablas en sql)

#Actualizar tablas
#1.- Se agrega los cambios a las tablas
#2.- se ejecuta ** python manage.py makemigrations (crea el 0002 en migrations)

# Crear super usuario
# python manage.py createsuperuser
#despues arrancar el servidor denuevo manage.py runserver
