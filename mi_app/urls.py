
from django.urls import path
from .views import (
    ProductoListView,
    ProductoCreateView,
    ProductoDetailView,
    ProductoUpdateView,
    ProductoDeleteView,

)

urlpatterns = [
    path("", ProductoListView.as_view(), name="lista_productos"),
    path("crear", ProductoCreateView.as_view(), name = "crear_producto"),
    path("producto/detalle/<int:pk>", ProductoDetailView.as_view(), name="detail_producto"),
    path("producto/actualizacion/<int:pk>", ProductoUpdateView.as_view(), name="update_producto"),
    path("producto/borrar/<int:pk>", ProductoDeleteView.as_view(), name = "borrar_producto"),

]
