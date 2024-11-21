from django.contrib import admin
from .models import User, Match


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'role')  # Columnas visibles en el listado
    list_filter = ('role',)  # Filtro por rol
    search_fields = ('name', 'email')  # Barra de búsqueda
    ordering = ('id',)  # Ordenar por ID


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'company', 'status', 'created_at')  # Columnas visibles en el listado
    list_filter = ('status',)  # Filtro por estado
    search_fields = ('student__name', 'company__name')  # Barra de búsqueda por nombre
    ordering = ('-created_at',)  # Ordenar por fecha de creación descendente
