from django.urls import path
from . import views
from .views import MyTokenOtbainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoutes),

    path('register/', views.register_user, name='register'),
    path('delete/', views.delete_user, name='delete'),
    
    path('token/', MyTokenOtbainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]