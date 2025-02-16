from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

# Vue d'inscription
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]  # N'importe qui peut s'inscrire
    serializer_class = UserSerializer

# Vue pour récupérer les détails d'un utilisateur (profil)
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]  # Un utilisateur doit être authentifié
    serializer_class = UserSerializer

# Vue pour lister les utilisateurs (uniquement accessible aux utilisateurs authentifiés)
@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Appliquer la permission ici
def list_users(request):
    users = User.objects.all()  # Récupérer tous les utilisateurs
    serializer = UserSerializer(users, many=True)  # Sérialiser les données
    return Response(serializer.data, status=status.HTTP_200_OK)
