from django.contrib import admin

from todolist.models import ToDoList

# Register your models here.
@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'is_completed',
                     'created_at')
    list_filter = ('title', 'created_at', 'is_completed')
    search_fields = ('title', 'is_completed', 'created_at',)