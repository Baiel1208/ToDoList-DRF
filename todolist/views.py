from rest_framework import mixins, status
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import DestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import ToDoList
from .serializers import ToDoListSerializer
from .permissions import ToDoListPermission
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


    def get_permissions(self):
        if self.action in ('create','update', 'destroy'):
            return (ToDoListPermission(), )
        return (AllowAny(), )
    
    # def get_serializer_class(self):
    #     if self.action in ('create', ):
    #         return UserRegisterSerializer
    #     if self.action in ('retrieve', ):
    #         return UserDetailSerializer
            
    #     return ToDoSerializer


class ToDoListAllDeleteAPIView(APIView):
    def delete(self, request, *args, **kwargs):
        todos = ToDoList.objects.filter(user=request.user)
        todos.delete()
        return Response({'delete': 'Все задания удалены'}, status=status.HTTP_204_NO_CONTENT)
# class ToDoListAllDeleteAPIView(DestroyAPIView):
#     queryset = ToDoList.objects.all()
#     serializer_class = ToDoListSerializer
#     permission_classes = [IsAuthenticated]
#     lookup_field = 'id'


    # def get_queryset(self):
    #     user = self.request.user
    #     return ToDoList.objects.filter(user=user)

    # def perform_destroy(self, instance):
    #     instance.delete()
    # def destroy(self, request, *args, **kwargs):
    #     super().destroy(request, *args, **kwargs)
    #     return Response({'delete' : 'Задачи успешно удалены'}, status=status.HTTP_200_OK)