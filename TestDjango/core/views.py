from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')



def datos(request):
    # contexto={"nombre":"Raul "}
    #recibir desde una clase
    hijo=Class_persona("Martin cabrera","23")
    contexto={"nombre":"Raul ","pariente":hijo}
    return render(request, 'datos.html',contexto) #  crear un diccionario llamado contexto
    


#creando una clase en python
class Class_persona:
    def __init__(self,nombre,edad):
         self.nombre=nombre
         self.edad=edad
         super().__init__()

