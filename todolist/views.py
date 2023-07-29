from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import DestroyAPIView

from .models import ToDoList
from .serializers import ToDoListSerializer
# Create your views here.

class ToDoListAPIView(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    GenericViewSet
                    ):

    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer
    
    # def get_serializer_class(self):
    #     if self.action in ('create', ):
    #         return UserRegisterSerializer
    #     if self.action in ('retrieve', ):
    #         return UserDetailSerializer
            
    #     return ToDoSerializer


class ToDoListAllDeleteAPIView(DestroyAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer


    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)