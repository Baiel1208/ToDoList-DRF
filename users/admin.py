from django.contrib import admin

from users.models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'date_joined', 'age',)
    list_filter = ('date_joined', 'age',)
    search_fields = ('username', 'email', 'phone_number',)