from django.db import models

from users.models import User

# Create your models here.
class ToDoList(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_todo",
        verbose_name="Пользователь"
    )
    title  = models.CharField(
        max_length=255, verbose_name='Название', unique=True
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='todo_image',verbose_name='Изображение',
        blank=True, null=True
    )
    is_completed = models.BooleanField(
        default=False, verbose_name='Завершено'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата и время создание'
    )


    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Список дел"
        verbose_name_plural = "Список дел"