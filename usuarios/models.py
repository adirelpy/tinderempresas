from django.db import models


class User(models.Model):
    ROLE_CHOICES = [
        ('student', 'Estudiante'),
        ('company', 'Empresa'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Nota: En producción, cifra las contraseñas
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    skills = models.TextField(blank=True, null=True)  # Solo para estudiantes
    requirements = models.TextField(blank=True, null=True)  # Solo para empresas

    def __str__(self):
        return f"{self.name} ({self.get_role_display()})"


class Match(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('accepted', 'Aceptado'),
        ('rejected', 'Rechazado'),
    ]

    student = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='student_matches',
        limit_choices_to={'role': 'student'},  # Asegura que solo estudiantes puedan ser asignados
    )
    company = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='company_matches',
        limit_choices_to={'role': 'company'},  # Asegura que solo empresas puedan ser asignadas
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.company.name} ({self.get_status_display()})"
