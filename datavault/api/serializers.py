from rest_framework import serializers
from .models  import Users
from django.contrib.auth.hashers import make_password , BCryptSHA256PasswordHasher

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Users
        fields = ['username','email','password','created_on','is_active','is_staff','is_superuser']
    
    def create(self,validated_data):
        hasher = BCryptSHA256PasswordHasher()
        salt = hasher.salt()
        validated_data["password"] = make_password(validated_data.get("password") , salt=salt,hasher=hasher , )
        return Users.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.username = validated_data.get("username",instance.username)
        instance.email = validated_data.get("email",instance.email)
        instance.is_active = validated_data.get("is_active",instance.is_active)
        instance.is_staff = validated_data.get("is_staff",instance.is_admin)
        instance.save()
        return instance
    