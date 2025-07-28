from django.shortcuts import render

from django.urls import reverse_lazy
from .models import Producto 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

"""
def hola(request):
    return render(request, "hola.html")


def listar_productos(request):
    productos = Producto.objects.all()   #query  ---  lee bd
    return render(request, "lista_de_productos.html", {"productos":productos})

"""

class ProductoListView(ListView):
    model = Producto
    template_name = "productos/producto_list.html"
    context_object_name = "productos"

class ProductoDetailView(DetailView):
    model = Producto
    template_name = "productos/producto_detail.html"
    context_object_name = "producto"

class ProductoCreateView(CreateView):
    model = Producto
    template_name = "productos/producto_form.html"
    field = ["nombre","descripcion", "precio", "stock", "image"]
    succes_url = reverse_lazy("lista_productos")

class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = "productos/producto_form.html"
    field = ["nombre","descripcion", "precio", "stock", "image"]
    succes_url = reverse_lazy("lista_productos")


class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "productos/producto_confirm.html"
    field = ["nombre","descripcion", "precio", "stock", "image"]
    succes_url = reverse_lazy("productos")



 

 