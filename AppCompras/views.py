from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Listas, DetalleLista
from django.contrib.auth.models import User
from .forms import UserForm, AddListForm, AddItemForm
from django.shortcuts import get_object_or_404
from django.core.checks import messages
# Create your views here.

@login_required(login_url='/login')
def home(request):
    listas= Listas.objects.filter(users=request.user.id)
    return render(request,"AppCompras/plantillas/home.html",{"listas":listas})

def lista(request, nombre_lista):
    lista = get_object_or_404(Listas, nombre=nombre_lista)
    detalles = DetalleLista.objects.filter(lista=lista)  # Filtra los objetos DetalleLista por la lista
    return render(request,"AppCompras/plantillas/detalle_lista.html",{"lista":detalles,"nombre":lista.nombre})


def add_user(request,nombre_lista):
    lista = get_object_or_404(Listas, nombre=nombre_lista)
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            usuario = User.objects.get(username=form.cleaned_data.get('nombre'))
            lista.users.add(usuario)
            return redirect("Home")
    else:
        form = UserForm()
        return render(request, "AppCompras/plantillas/add_user.html", {'form':form})


def nueva_lista(request):
    if request.method == 'POST':
        form = AddListForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data.get("nombre")
            new_list = Listas.objects.create(nombre=nombre )
            new_list.users.add(request.user)
            new_list.save()

            return redirect("Home")
    else:
        form = AddListForm()

        return JsonResponse({'form': form.as_p()})

def editar_lista(request, id):
    lista = get_object_or_404(Listas, id=id)
    if request.method == 'POST':
        form = AddListForm(request.POST)
        if form.is_valid():
            lista.nombre = form.cleaned_data.get("nombre")


            lista.save()

            return redirect("Home")
    else:
        form = AddListForm(instance=lista)
        return JsonResponse({'form': form.as_p()})

def nuevo_elemento(request,nombre_lista):
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data.get("nombre")
            cantidad = form.cleaned_data.get("cantidad")
            lista = get_object_or_404(Listas, nombre=nombre_lista)
            new_list = DetalleLista.objects.create(nombre=nombre,lista=lista,cantidad=cantidad)

            new_list.save()

            return redirect("lista", nombre_lista=nombre_lista)
    else:
        form = AddItemForm()

        return JsonResponse({'form': form.as_p()})

def editar_elemento(request,nombre_lista, id):
    elemento = get_object_or_404(DetalleLista, id=id)
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            elemento.nombre = form.cleaned_data.get("nombre")
            elemento.cantidad = form.cleaned_data.get("cantidad")

            elemento.save()

            return redirect("lista", nombre_lista=nombre_lista)
    else:
        form = AddItemForm(instance=elemento)
        return JsonResponse({'form': form.as_p()})


def delete_item(request,nombre_lista,id):
    objeto = get_object_or_404(DetalleLista, id=id)
    objeto.delete()
    return redirect("lista", nombre_lista=nombre_lista)


def delete_lista(request,id):
    objeto = get_object_or_404(Listas, id=id)
    objeto.delete()
    return redirect("Home")


def autenticacion(request):
    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(username=usuario, password=contra)
            if usuario:
                login(request, usuario)
                return redirect("Home")
            else:
                messages.error(request, "Usuario invalido")
        else:
            messages.error(request, "Usuario invalido")
    form = AuthenticationForm()
    form.css_class = 'formulario_login'

    return render(request, "AppCompras/plantillas/login.html", {"form": form})