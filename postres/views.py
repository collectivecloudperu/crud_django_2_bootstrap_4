from django.shortcuts import render

from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Postres

from django.urls import reverse

from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 

from django import forms

class PostresListado(ListView): 
    model = Postres

class PostreDetalle(DetailView): 
    model = Postres

class PostreCrear(SuccessMessageMixin, CreateView): 
    model = Postres
    form = Postres
    fields = "__all__" 
    success_message = 'Postre Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre     

    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer' 

class PostreActualizar(SuccessMessageMixin, UpdateView): 
    model = Postres
    form = Postres
    fields = "__all__"  
    success_message = 'Postre Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer' 

class PostreEliminar(SuccessMessageMixin, DeleteView): 
    model = Postres 
    form = Postres
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Postre Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'                    