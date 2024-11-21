from django.urls import path
from . import views

urlpatterns = [
    # Listar usuarios en HTML (Frontend)
    path("list-template/", views.list_users_template, name="list_users_template"),

    # Crear usuario desde formulario (Frontend)
    path("create-template/", views.create_user_template, name="create_user_template"),

    # Editar usuario desde formulario (Frontend)
    path("edit-template/<int:user_id>/", views.edit_user_template, name="edit_user_template"),

    # Eliminar usuario desde formulario (Frontend)
    path("delete-template/<int:user_id>/", views.delete_user_template, name="delete_user_template"),

    # Crear usuario (API JSON)
    path("create/", views.create_user, name="create_user"),

    # Listar usuarios (API JSON)
    path("list/", views.list_users, name="list_users"),

    # Actualizar usuario (API JSON)
    path("update/<int:user_id>/", views.update_user, name="update_user"),

    # Eliminar usuario (API JSON)
    path("delete/<int:user_id>/", views.delete_user, name="delete_user"),

    # Rutas del sistema de matching
    # Crear un match (API JSON)
    path("match/create/", views.create_match, name="create_match"),

    # Listar matches (API JSON)
    path("match/list/", views.list_matches, name="list_matches"),

    # Actualizar estado de un match (API JSON)
    path("match/update/<int:match_id>/", views.update_match_status, name="update_match_status"),

    # Eliminar un match (API JSON)
    path("match/delete/<int:match_id>/", views.delete_match, name="delete_match"),
]
