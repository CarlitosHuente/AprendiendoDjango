from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article, Category
from django.db.models import Q
from miapp.forms import FormArticle
from django.contrib import messages

# Create your views here.
#MVC = Modelo Vista Controlador (Recibe info del usuario) -> Acciones (Metodos)

#MVT = Modelo Vista Template

layout = """

<h1> Sitio web con Django </h1>
<hr/>
<ul>
    <li>
        <a href="/inicio">Inicio <a/>
    </li>
    <li>
        <a href="/hola-mundo">Hola Mundo <a/>
    </li>
    <li>
        <a href="/pagina-pruebas">Pagina de Prueba<a/>
    </li>
    <li>
        <a href="/contacto">Contacto<a/>
    </li>
</ul>
<hr/>
"""


def index(request):
    """
    html = 
            <h1> Inicio </h1>
            <p> Años hasta el 2050</p>
            <ul>
    
    year = 2021
    while year <= 2050:
        html += f"<li>{str(year)}</li>"
        year += 1

    html += "</ul>"
    """

    year = 2021
    hasta = range(year,2050)

    nombre = 'Carlos Carvajal Reyes'

    lenguajes = ['javascrips', 'python', 'PHP', 'C']

    return render(request, 'index.html',
    {'mi_variable':'soy un dato que esta en la vista',
     'nombre' : nombre,
     'lenguajes':lenguajes,
     'years':hasta
     })


def hola_mundo(request):
    return render(request,'hola_mundo.html')


def pagina(request, redirigir = 0):

    if redirigir == 1:
        return redirect('/inicio')

    return render(request, 'pagina.html',
        {'texto' :'',
         'lista':['uno','dos','tres']

        })

def contacto(request, nombre="", apellidos=""):
    html = ""
    if nombre and apellidos:
        html += "El nombre completo es :"
        html += f"<h3>{nombre} {apellidos} </h3>"
    ""

    return HttpResponse(layout +f"""
        <h2> Contacto {nombre} {apellidos}</h2>

    """)
#crear en GET
def crear_articulo(request, title, content, public):
    articulo = Article(
        title= title,
        content= content,
        public = public
    )
    articulo.save()

    return HttpResponse(f"Articulo Creado: {articulo.title}")
#Crear en GET/POST
def save_article(request):

    if request.method =="POST":

        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']
        articulo = Article(
            title= title,
            content= content,
            public = public
        )
        articulo.save()
        return HttpResponse(f"Articulo Creado: {articulo.title}")
    else:
        return HttpResponse("No se ha podido crear el articulo")

def create_article(request):

    return render(request,'create_article.html')

def create_full_article(request):

    if request.method == 'POST':
        formulario = FormArticle(request.POST)

        if formulario.is_valid():
            data_form= formulario.cleaned_data

            title= data_form.get('title')
            content= data_form['content']
            public= data_form['public']

            articulo = Article(
            title= title,
            content= content,
            public = public
            )

            articulo.save()

            #Mensaje Flash (Emergente)
            messages.success(request,f'Has Creado correctamente el articulo {articulo.id}')

        
            #return HttpResponse(title + '-' + content + '-' + str(public))
            return redirect('articulos')

    else:
        formulario = FormArticle()
    
    return render(request, 'create_full_article.html',{
                  'form':formulario
    })


def articulo(request):

    try:
        articulo = Article.objects.get(pk=8) #con el get se hace la consulta con el nombre del atributo[con , se agrega mas condiciones]
        response = f"Articulo: {articulo.title}"
    except:
        response = "Articulo no encontrado"
    return HttpResponse(response)

def editar_articulo(request, id):
    articulo = Article.objects.get(pk=id)

    articulo.title = "Batman"
    articulo.content = "Pelicula 2017"
    articulo.public = True
    articulo.save()

    return HttpResponse (f"Articulo Modificado: {articulo.title}")

def articulos(request):

    articulos=Article.objects.order_by('-id')[:20]#Es lo mismo q el get, pero se muestra todo los [] es para limitar la cantidad q aparece
                                        # Tambien [desde : Hasta ]

    #articulos = Article.objects.filter(title__contains='o')#contains permite buscar que contenga [lookup]
    #articulos = Article.objects.filter(id__gt=11)
    #LookUp |gt:mayor que |gte:Mayor o igual |lt:menor que |lte:Menor o igual

    #articulos = Article.objects.filter(title__contains="o").exclude(title__contains="3")
    #articulos = Article.objects.filter(Q(title__contains="3")|Q(title__contains="4")) #Es como el "O" pero hay q importar "Q"


    #articulos = Article.objects.raw("SELECT * FROM  miapp_article")# sql pura




    return render(request,'articulos.html',{
        'articulos':articulos
    })

def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect('articulos')