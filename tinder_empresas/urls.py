from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Página inicial simple
def home(request):
    return HttpResponse("¡Bienvenido a Tinder para Empresas!")

urlpatterns = [
    path('admin/', admin.site.urls),               # Ruta para el panel de administración
    path('', home, name='home'),                   # Página inicial
    path('usuarios/', include('usuarios.urls')),  # Rutas de la app usuarios
]
