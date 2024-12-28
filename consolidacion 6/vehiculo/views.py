from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .forms import VehiculoForm
from .models import Vehiculo

# Create your views here.


def index(request):
    return render(request, 'vehiculo/index.html')


def redirect_to_index(request):
    return redirect('index')


def add_vehicle(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/add_vehicle.html', {'form': form})


@login_required
@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
def list_vehicles(request):
    vehicles = Vehiculo.objects.all()
    for vehicle in vehicles:
        if vehicle.precio < 10000:
            vehicle.condicion_precio = 'Bajo'
        elif 10000 <= vehicle.precio <= 30000:
            vehicle.condicion_precio = 'Medio'
        else:
            vehicle.condicion_precio = 'Alto'
    return render(request, 'vehiculo/list_vehicles.html', {'vehicles': vehicles})
