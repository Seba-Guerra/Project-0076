from django.shortcuts import get_object_or_404, render, redirect
from .models import Laboratorio
from .forms import LaboratorioForm


def laboratorio_list(request): 
    # Contador de visitantes 
    if 'visits' in request.session: 
        request.session['visits'] += 1 
    else: 
        request.session['visits'] = 1 
    laboratorios = Laboratorio.objects.all() 
    return render(request, 'laboratorio/laboratorio_list.html', {'laboratorios': laboratorios})


def laboratorio_create(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('laboratorio_list')
    else:
        form = LaboratorioForm()  # Este bloque crea un formulario vacío para solicitudes GET.
    
    return render(request, 'laboratorio/laboratorio_form.html', {'form': form})

def laboratorio_update(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('laboratorio_list')
    else:
        form = LaboratorioForm(instance=laboratorio)
    return render(request, 'laboratorio/laboratorio_form.html', {'form': form})


def laboratorio_delete(request, pk): 
    laboratorio = get_object_or_404(Laboratorio, pk=pk) 
    if request.method == 'POST': 
        laboratorio.delete() 
        return redirect('laboratorio_list') 
    return render(request, 'laboratorio/laboratorio_confirm_delete.html', {'laboratorio': laboratorio})

def laboratorio_detail(request, pk): 
    laboratorio = get_object_or_404(Laboratorio, pk=pk) 
    return render(request, 'laboratorio/laboratorio_detail.html', {'laboratorio': laboratorio})