from ast import Return
from multiprocessing import context
from django.shortcuts import render, HttpResponse
import random
import datetime
import rutas

# Create your views here.
def home(request):
    resp = request.GET.get('home') 
    contexto = {}
    contexto["result"] = 'Soy estudiante egresado de la carrera de Analista Programador del Centro de Formación Técnica de INACAP (2022). Actualmente, en continuidad de estudios de pregrado, ingresando a la carrera de Ingeniería en Informática del Instituto Profesional de INACAP. (2023).'
    contexto["result2"] = 'Este trabajo fue realizado mientras cursaba el 4° semestre de la carrera, en el ramo Programación Backend. Es una página web muy sencilla que tuvo como objetivo realizar una Introducción a la programación del lado del servidor, de acuerdo con la sintaxis del lenguaje con el framework de código abierto Django (Configuración, Rutas y Vistas) y bajo el patrón MVT.'
    return render(request,"rutas/home.html", context=contexto)
def primos(request):    
    resp = request.GET.get('primos')
    contexto = {}    
    num = 0
    x = 1
    lista = [0] * x
    todos = [0] * 25
    cont = -1
    for x in range (1,101):
        num = x 
        primo = 0
        x = 1
        while x <= num:        
            if num % x == 0:        
                primo = primo + 1                    
            x = x + 1   
        if primo == 2:            
            lista = (num)             
            cont = cont + 1
        todos[cont] = (lista)
    
    contexto["result"] = (todos)    
    return render(request,"rutas/primos.html",context=contexto)

def factorial(request):
    resp = request.GET.get('factorial')
    contexto = {}

    notacion = (random.randrange(5, 11))
    numFact = 1
    i = 0
    x = 0
    while i < notacion:
        i = i + 1    
        x = i
        numFact = 1
        while x >= 1:
            numFact = numFact * x
            x = x - 1
    contexto["result"] = (f"{notacion}! = {numFact}")

    return render(request,"rutas/factorial.html", context=contexto)

def saludo(request):
    resp = request.GET.get('saludo')
    contexto = {}
    if resp is None:
        x = datetime.datetime.now()
        hora = x.hour
        if hora >=0 and hora <= 12:
            contexto["result"] = "¡Buenos Días!"  
        else:
            if hora > 12 and hora <= 20:
                contexto["result"] = "¡Buenas Tardes!"
            else:
                if hora > 20 and hora <= 23:
                    contexto["result"] = "¡Buenas Noches!"       
    return render(request,"rutas/saludo.html", context=contexto)
