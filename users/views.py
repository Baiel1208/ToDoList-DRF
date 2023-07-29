from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from users.models import User

from .serializers import UserSerializer,UserRegisterSerializer,UserDetailSerializer
# Create your views here.

class UserAPIView(GenericViewSet,
                     mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_serializer_class(self):
        if self.action in ('create', ):
            return UserRegisterSerializer
        if self.action in ('retrieve', ):
            return UserDetailSerializer
        return UserSerializer