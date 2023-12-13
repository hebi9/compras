from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('nueva_lista/', views.nueva_lista, name="nueva_lista"),
    path('login/', views.autenticacion, name="autenticacion"),
    path('editar_lista/<int:id>/', views.editar_lista, name="editar_lista"),
    path('delete_lista/<int:id>/', views.delete_lista, name="delete_lista"),
    path('<nombre_lista>/', views.lista, name="lista"),
    path('<nombre_lista>/nuevo_elemento/', views.nuevo_elemento, name="nuevo_elemento"),
    path('<nombre_lista>/add_user/', views.add_user, name="add_user"),
    path('<nombre_lista>/delete_item/<int:id>/', views.delete_item, name="delete_item"),
    path('<nombre_lista>/editar_elemento/<int:id>/', views.editar_elemento, name="editar_elemento"),

]
