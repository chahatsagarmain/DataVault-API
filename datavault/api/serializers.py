from rest_framework import serializers
from .models  import Users

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Users
        fields = ['user_name','email','password','created_on','is_active','is_admin']
    
    def create(self,validated_data):
        return Users.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.user_name = validated_data.get("user_name",instance.user_name)
        instance.email = validated_data.get("email",instance.email)
        instance.is_active = validated_data.get("is_active",instance.is_active)
        instance.is_admin = validated_data.get("is_admin",instance.is_admin)
        instance.save()
        return instance