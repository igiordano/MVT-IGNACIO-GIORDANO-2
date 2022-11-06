from django.shortcuts import render

from MiApp.models import Familia
# Create your views here.

def mostrar_familia(request):

    f1 = Familia(nombre='Miguel', apellido='Giordano', edad=64, cumpleanios='1958-07-30')
    f2 = Familia(nombre='Ignacio', apellido='Giordano', edad=31, cumpleanios='1991-03-15')
    f3 = Familia(nombre='Victoria', apellido='Giordano', edad=35, cumpleanios='1986-10-06')
    f4 = Familia(nombre='Monica', apellido='Cora', edad=61, cumpleanios='1961-02-15')

    return render(request, 'MiApp/familia.html',{'familia':[f1, f2, f3, f4]})