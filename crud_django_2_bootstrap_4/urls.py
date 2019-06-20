"""crud_django_2_bootstrap_4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from django.views.generic import TemplateView
from postres.views import PostresListado, PostreDetalle, PostreCrear, PostreActualizar, PostreEliminar
#from . import views

#from postres.views import PostresList

from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('postres/', PostresListado.as_view(template_name = "postres/index.html"), name='leer'),
    path('postres/detalle/<int:pk>', PostreDetalle.as_view(template_name = "postres/detalles.html"), name='detalles'), 
    path('postres/crear', PostreCrear.as_view(template_name = "postres/crear.html"), name='crear'),
    path('postres/editar/<int:pk>', PostreActualizar.as_view(template_name = "postres/actualizar.html"), name='actualizar'),    
    path('postres/eliminar/<int:pk>', PostreEliminar.as_view(), name='eliminar'),    
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
