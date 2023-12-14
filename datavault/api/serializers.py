from rest_framework import serializers
from .models  import Users

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Users
        fields = ['user_name','email','password','created_on','is_active','is_admin']
    
    def create(self,validated_data):
        return Users.objects.create(**validated_data)
        