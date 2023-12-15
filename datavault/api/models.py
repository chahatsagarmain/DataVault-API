from django.db import models
from django.contrib.auth.models import UserManager , AbstractBaseUser , PermissionsMixin

class Users(AbstractBaseUser,PermissionsMixin):
    
    username = models.CharField(max_length=128,
                                blank=False,
                                verbose_name="username" , unique = True)
    
    email = models.EmailField(verbose_name="user_email",
                              max_length=50,
                              null=False)
    
    password = models.CharField(verbose_name="user_password",
                                max_length=256,
                                null=False)
    
    created_on = models.DateTimeField(verbose_name="created_on",
                                auto_now_add=True)

    is_active = models.BooleanField(default=True)
    
    is_admin = models.BooleanField(default=False)
    
    objects = UserManager()
    
    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'
    
    @property
    def is_admin(self):
            return self.is_admin
        
    def __str__(self):  
         return self.username
    
        

class FileInfo(models.Model):

    user_id = models.ForeignKey("Users",on_delete=models.CASCADE)
    
    file_date = models.DateField(auto_now_add=True)
    
    file_compressed = models.BooleanField(default=False)
    
    
class Files(models.Model):
    
    file_id = models.ManyToManyField("FileInfo")
    
    file_path = models.CharField(max_length=256)
    
    file_size = models.PositiveIntegerField("file size(in Bytes)")
        