from django.contrib import admin 
from .models import Users,FileInfo,Files

# Register your models here.

@admin.register(Users)
class UsersAdminModel(admin.ModelAdmin):
    list_display = ('username','email','created_on','is_active','is_staff' ,'is_superuser')
    
    class Meta:
        ordering = ('id')


