from django.http import HttpResponse

#Request: Para realizar peticiones
#HttpResponse: Para enviar la respuesta usando el protocolo HTTP

#Esto es una vista:
def bienvenida(request): #Pasamos un objeto de tipo request
    return HttpResponse("Hola mundo")
def categoriaEdad(request,edad):
    if edad >= 18:
        if edad >= 60:
            categoria= "Tercera edad"
        else:
            categoria= "Adultez"
    else:
        if edad <10:
            categoria= "Infancia"
        else:
            categoria= "Adolescencia"
    resultado= "<h2><p style='color:green;'>Categoria de la edad:"+categoria+"</p></h2> "
    return HttpResponse(resultado)