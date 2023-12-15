from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import Users
import rest_framework.status
from .utils import encrypt_password
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class UserViews(APIView):
    
    # Fetch a user 
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
        
    def get(self, request, id):
        try:
            user_raw = Users.objects.get(id=id)
            serialized_user = UserSerializer(user_raw) 
            response = {
                "username" : serialized_user.data['username'],
                "email" : serialized_user.data["email"],
                "created_on" : serialized_user.data["created_on"],
                "is_active" : serialized_user.data["is_active"],
                "is_admin" : serialized_user.data["is_admin"]
            }
            
            return Response(response, status=rest_framework.status.HTTP_202_ACCEPTED)
        
        except Users.DoesNotExist as e:
            response = {"message": "User does not exist"}
            return Response(response, status=rest_framework.status.HTTP_404_NOT_FOUND)
    
        except Exception as e:
            response = {"message": str(e)}
            return Response(response, status=rest_framework.status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self , request):
        try:
            data = request.data
            serialized = UserSerializer(data = data)

            if serialized.is_valid():
                user_data = serialized.data
                password = user_data.get("password")
                
                # if password:
                #     encrypted_password = encrypt_password(password)
                #     user_data["password"] = encrypted_password
                    
                
                user_instance = serialized.create(validated_data=user_data)
                
                return Response({"message" : "User created",
                                 "user_id" : user_instance.id} , 
                                status=rest_framework.status.HTTP_201_CREATED)
            
            else:
                return Response(serialized.errors , status=rest_framework.status.HTTP_406_NOT_ACCEPTABLE)
                  
        
        except Exception as e:
            print(e)
            return  Response({"message" : str(e)} , status=rest_framework.status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self , request , id=None,username=None):
        print(username)
        try:
            if id is not None :
                data = request.data
                serialized_data = UserSerializer(data = data)

                if serialized_data.is_valid():
                    user = Users.objects.get(id = id)
                    updated_user = serialized_data.update(user,serialized_data.data)
                    serialized_updated_user = UserSerializer(updated_user)
                    response = {"message" : "User updated" , "updated_user" : serialized_updated_user.data}
                    return Response(response , status=rest_framework.status.HTTP_202_ACCEPTED)

                else:
                    response = {"message" : serialized_data.errors}

                    return Response(response , status=rest_framework.status.HTTP_406_NOT_ACCEPTABLE)
                
            if username is not None:
                data = request.data
                serialized_data = UserSerializer(data = data)

                if serialized_data.is_valid():
                    user = Users.objects.get(username = username)
                    updated_user = serialized_data.update(user,serialized_data.data)
                    serialized_updated_user = UserSerializer(updated_user)
                    response = {"message" : "User updated" , "updated_user" : serialized_updated_user.data}
                    return Response(response , status=rest_framework.status.HTTP_202_ACCEPTED)

                else:
                    response = {"message" : serialized_data.errors}

                    return Response(response , status=rest_framework.status.HTTP_406_NOT_ACCEPTABLE)
            
        
        except Users.DoesNotExist as e:
            response = {"message" : str(e)}
            
            return Response(response , status=rest_framework.status.HTTP_404_NOT_FOUND)
        
        except Exception as e :
            response = {"message" : str(e)}
            
            return Response(response,status=rest_framework.status.HTTP_500_INTERNAL_SERVER_ERROR)
            

    
    def delete(self , request , id):
        try:
            user = Users.objects.get(id = id)
            user.delete()
            response = {"message" : "User deleted"}
            return Response(response,status=rest_framework.status.HTTP_200_OK)
        
        except Users.DoesNotExist:
            response = {"message" : "User does not exist"}
            return Response(response,status=rest_framework.status.HTTP_404_NOT_FOUND)
            
        except Exception as e:
            response = {"message" : f"Error occured {str(e)}"}
            return Response(response , status=rest_framework.status.HTTP_500_INTERNAL_SERVER_ERROR)

class LoginViews(APIView):
    
    def post(self,request):
        
    


class FileViews(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        pass