from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import ToDoListAPIView, ToDoListAllDeleteAPIView

router = DefaultRouter()
router.register('todolist', ToDoListAPIView, 'api_todolist')

urlpatterns = [
    path('delete/all/', ToDoListAllDeleteAPIView.as_view(), name = "todolist_all_delete"),
]


urlpatterns += router.urls