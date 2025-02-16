from django.urls import path
from .views import CustomTokenObtainPairView, RegisterView, UserDetailView, list_users

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterView.as_view(), name='register_user'),
    path('user/', UserDetailView.as_view(), name='user_detail'),
    path('users/', list_users, name='list_users'),
]
