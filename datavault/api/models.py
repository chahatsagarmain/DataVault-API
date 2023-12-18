from django.db import models
from django.contrib.auth.models import UserManager , AbstractBaseUser , PermissionsMixin
import datetime

class Users(AbstractBaseUser,PermissionsMixin):
    
    username = models.CharField(max_length=128,
                                blank=False,
                                verbose_name="username" , unique = True)
    
    email = models.EmailField(verbose_name="user_email",
                              max_length=50,
                              unique=True,
                              null=False)
    
    password = models.CharField(verbose_name="user_password",
                                max_length=256,
                                null=False)
    
    created_on = models.DateTimeField(verbose_name="created_on",
                                auto_now_add=True)

    is_active = models.BooleanField(default=True)
    
    is_staff = models.BooleanField(default=False)

    is_admin = models.BooleanField(default = False)  
    
      
    
    objects = UserManager()
    
    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'
        
    def __str__(self):  
         return self.username
    
        
    
class Files(models.Model):
   
    user_id = models.ForeignKey('Users',on_delete=models.CASCADE)

    file_name = models.CharField(db_column='name', max_length=200, default="file_name",unique=True)
    
    file_store = models.FileField(upload_to=f"./uploads/{datetime.datetime.now()}")
    
    def __str__(self):
        return self.file_name 
    
    
        # def create(self,*args,**kwargs):