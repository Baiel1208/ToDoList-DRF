from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserAPIView, UserRegisterAPIView

router = DefaultRouter()
router.register('user', UserAPIView, 'api_users')

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view({'post': 'create'}), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
]


urlpatterns += router.urls