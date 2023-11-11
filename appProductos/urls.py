from django.urls import path
from . import views

#Se agrega un comentario de prueba
# Comentario para modificar el archivo
urlpatterns = [
    path('producto/', views.verProductos, name="productos"),
    path('producto/<str:id>', views.verProductos, name="producto"), 
    path('carrito/<str:id>', views.agregar, name="carrito"),
    path('vercarrito/', views.verCarrito, name="ver_carrito"),
    path('eliminar/<str:id>', views.eliminarItemCarrito, name="eliminar"),
    path('cambiarCantidad/', views.cambiarCantidad),
]

