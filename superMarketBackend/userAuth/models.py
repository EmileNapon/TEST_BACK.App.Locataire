from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_manager(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('role', 'manager')  # Définir le rôle à 'manager' par défaut
        return self.create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin')  # Définir le rôle à 'admin' par défaut
        return self.create_user(email, password, **extra_fields)  # Appeler create_user pour créer le super utilisateur

class User(AbstractUser):
    ROLE_CHOICES = [
        ("citizen", "citoyen"),
        ("authority", "autorité"),
        ("supplier", "entreprise"),
        ("admin", "administrateur"),
    ]
    username=models.CharField(max_length=20, null=True)
    first_name=models.CharField(max_length=20, null=True, default='Napon')
    last_name=models.CharField(max_length=20, null=True, default='Emile')
    # Attributs supplémentaires
    email = models.EmailField(unique=True)  # Rendre l'email unique
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="citizen")
    phone_number = models.CharField(max_length=20, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    # Attributs Citoyen
    profession = models.CharField(max_length=100, blank=True, null=True)
    enabled_notifications = models.BooleanField(default=True)

    # Attributs Autorité
    name_organization = models.CharField(max_length=100, blank=True, null=True)

    # Attributs Prestataire
    nom_entreprise = models.CharField(max_length=100, blank=True, null=True)
    secteur_activite = models.CharField(max_length=100, blank=True, null=True)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["role"]  # 'role' doit être obligatoire lors de la création

    # Définit le gestionnaire
    objects = UserManager()

    def __str__(self):
        return f"{self.role} - {self.email}"
