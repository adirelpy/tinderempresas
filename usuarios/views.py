from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password  # Para cifrar contraseñas
from .models import User, Match
import json

# Crear un usuario (JSON)
@csrf_exempt
def create_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user = User.objects.create(
                name=data.get("name"),
                email=data.get("email"),
                password=make_password(data.get("password")),  # Cifrar contraseñas
                role=data.get("role"),
                skills=data.get("skills", ""),
                requirements=data.get("requirements", ""),
            )
            return JsonResponse({"message": "Usuario creado con éxito", "id": user.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": f"Error al crear usuario: {str(e)}"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

# Crear un usuario desde el formulario HTML
def create_user_template(request):
    if request.method == "POST":
        try:
            name = request.POST.get("name")
            email = request.POST.get("email")
            password = request.POST.get("password")
            role = request.POST.get("role")
            skills = request.POST.get("skills", "")
            requirements = request.POST.get("requirements", "")

            User.objects.create(
                name=name,
                email=email,
                password=make_password(password),  # Cifrar contraseñas
                role=role,
                skills=skills,
                requirements=requirements,
            )
            return redirect("list_users_template")
        except Exception as e:
            return JsonResponse({"error": f"Error al crear usuario: {str(e)}"}, status=400)
    return render(request, "usuarios/create_user.html")

# Leer todos los usuarios (JSON)
def list_users(request):
    if request.method == "GET":
        users = User.objects.all()
        users_data = [
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "role": user.role,
                "skills": user.skills,
                "requirements": user.requirements,
            }
            for user in users
        ]
        return JsonResponse({"users": users_data})
    return JsonResponse({"error": "Método no permitido"}, status=405)

# Listar usuarios en HTML (Frontend)
def list_users_template(request):
    users = User.objects.all()
    return render(request, "usuarios/list_users.html", {"users": users})

# Editar un usuario desde el formulario HTML
def edit_user_template(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        try:
            user.name = request.POST.get("name", user.name)
            user.email = request.POST.get("email", user.email)
            user.password = make_password(request.POST.get("password", user.password))  # Cifrar contraseñas
            user.role = request.POST.get("role", user.role)
            user.skills = request.POST.get("skills", user.skills)
            user.requirements = request.POST.get("requirements", user.requirements)
            user.save()
            return redirect("list_users_template")
        except Exception as e:
            return JsonResponse({"error": f"Error al editar usuario: {str(e)}"}, status=400)
    return render(request, "usuarios/edit_user.html", {"user": user})

# Actualizar un usuario (JSON)
@csrf_exempt
def update_user(request, user_id):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            user = get_object_or_404(User, id=user_id)
            user.name = data.get("name", user.name)
            user.email = data.get("email", user.email)
            user.password = make_password(data.get("password", user.password))  # Cifrar contraseñas
            user.role = data.get("role", user.role)
            user.skills = data.get("skills", user.skills)
            user.requirements = data.get("requirements", user.requirements)
            user.save()
            return JsonResponse({"message": "Usuario actualizado con éxito"})
        except Exception as e:
            return JsonResponse({"error": f"Error al actualizar usuario: {str(e)}"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

# Eliminar un usuario (JSON)
@csrf_exempt
def delete_user(request, user_id):
    if request.method == "DELETE":
        try:
            user = get_object_or_404(User, id=user_id)
            user.delete()
            return JsonResponse({"message": "Usuario eliminado con éxito"})
        except Exception as e:
            return JsonResponse({"error": f"Error al eliminar usuario: {str(e)}"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

# Eliminar un usuario desde el frontend
def delete_user_template(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        try:
            user.delete()
            return redirect("list_users_template")
        except Exception as e:
            return JsonResponse({"error": f"Error al eliminar usuario: {str(e)}"}, status=400)
    return render(request, "usuarios/delete_user.html", {"user": user})

# Crear un match
@csrf_exempt
def create_match(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            student = User.objects.get(id=data.get("student_id"), role="student")
            company = User.objects.get(id=data.get("company_id"), role="company")
            match = Match.objects.create(student=student, company=company)
            return JsonResponse({"message": "Match creado con éxito", "id": match.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": f"Error al crear match: {str(e)}"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

# Listar matches (JSON)
def list_matches(request):
    if request.method == "GET":
        matches = Match.objects.all()
        matches_data = [
            {
                "id": match.id,
                "student": match.student.name,
                "company": match.company.name,
                "status": match.status,
                "created_at": match.created_at,
            }
            for match in matches
        ]
        return JsonResponse({"matches": matches_data})
    return JsonResponse({"error": "Método no permitido"}, status=405)

# Actualizar el estado de un match
@csrf_exempt
def update_match_status(request, match_id):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            match = Match.objects.get(id=match_id)
            match.status = data.get("status", match.status)
            match.save()
            return JsonResponse({"message": "Estado del match actualizado con éxito"})
        except Match.DoesNotExist:
            return JsonResponse({"error": "Match no encontrado"}, status=404)
        except Exception as e:
            return JsonResponse({"error": f"Error al actualizar match: {str(e)}"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

# Eliminar un match
@csrf_exempt
def delete_match(request, match_id):
    if request.method == "DELETE":
        try:
            match = Match.objects.get(id=match_id)
            match.delete()
            return JsonResponse({"message": "Match eliminado con éxito"})
        except Match.DoesNotExist:
            return JsonResponse({"error": "Match no encontrado"}, status=404)
        except Exception as e:
            return JsonResponse({"error": f"Error al eliminar match: {str(e)}"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)
