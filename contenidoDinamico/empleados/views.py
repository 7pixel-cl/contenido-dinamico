from django.shortcuts import render

# Create your views here.


def empleados(request):
    empleados = ["Madelinne", "Juan", "Pedro", "Luis", "Ana", "Maria", "Matthew"]
    context = {"empleados": empleados}
    return render(request, "empleados.html", context)
