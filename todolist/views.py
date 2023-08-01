from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import DestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

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
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title', 'is_completed',]
    search_fields = ['title', 'is_completed', 'user__username']
    
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