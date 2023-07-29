from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(
        unique=True, verbose_name='Адрес электроной почты'
    )
    phone_number = models.CharField(
        max_length=16 ,unique=True, verbose_name="Номер телефона"
    )
    age = models.PositiveIntegerField(blank=True,null=True,
        verbose_name="Возраст"
    )


    def __str__(self):
        return self.username


    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

