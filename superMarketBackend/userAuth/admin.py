# from django.contrib import admin
# from .models import User, Citoyen, Autority, Supplier

# # Enregistrer le modèle Utilisateur
# @admin.register(Utilisateur)
# class UtilisateurAdmin(admin.ModelAdmin):
#     list_display = ['email_address', 'first_name', 'last_name', 'role', 'is_active', 'is_staff']
#     search_fields = ['email_address', 'first_name', 'last_name']

# # Enregistrer le modèle Citoyen
# @admin.register(Citoyen)
# class CitoyenAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'last_name', 'profession', 'birth_date', 'enabled_notifications']
#     search_fields = ['first_name', 'last_name']

# # Enregistrer le modèle Autority
# @admin.register(Autority)
# class AutorityAdmin(admin.ModelAdmin):
#     list_display = ['name_organization']
#     search_fields = ['name_organization']

# # Enregistrer le modèle Supplier
# @admin.register(Supplier)
# class SupplierAdmin(admin.ModelAdmin):
#     list_display = ['nom_entreprise', 'secteur_activite']
#     search_fields = ['nom_entreprise', 'secteur_activite']
