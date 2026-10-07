from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicamento
from .forms import MedicamentoForm

def inicio(request):
    total_medicamentos = Medicamento.objects.count()
    return render(request, 'farmaciaapp/inicio.html', {'total': total_medicamentos})

def listar_medicamentos(request):
    medicamentos = Medicamento.objects.all().order_by('nombre')
    return render(request, 'farmaciaapp/listar.html', {'medicamentos': medicamentos})

def crear_medicamento(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_medicamentos')
    else:
        form = MedicamentoForm()
    return render(request, 'farmaciaapp/crear.html', {'form': form})

def editar_medicamento(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    if request.method == 'POST':
        form = MedicamentoForm(request.POST, instance=medicamento)
        if form.is_valid():
            form.save()
            return redirect('listar_medicamentos')
    else:
        form = MedicamentoForm(instance=medicamento)
    return render(request, 'farmaciaapp/editar.html', {'form': form, 'medicamento': medicamento})

def eliminar_medicamento(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    if request.method == 'POST':
        medicamento.delete()
        return redirect('listar_medicamentos')
    return render(request, 'farmaciaapp/eliminar.html', {'medicamento': medicamento})