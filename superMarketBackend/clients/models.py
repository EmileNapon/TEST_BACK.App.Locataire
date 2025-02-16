from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django.contrib.auth.models import User

class Client(TenantMixin):
    name = models.CharField(max_length=100, unique=True)  # Nom unique du supermarché
    created_on = models.DateField(auto_now_add=True)  # Date d'inscription
    paid_until = models.DateField(null=True, blank=True)  # Abonnement payé jusqu'à
    on_trial = models.BooleanField(default=True)  # Supermarché en essai ?
    auto_create_schema =models.BooleanField(default=True)  # Crée automatiquement le schéma
    
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    

    def __str__(self):
        return self.name

class Domain(DomainMixin):
    pass

