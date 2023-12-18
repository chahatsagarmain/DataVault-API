from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer , FileUploadSerialiser
from rest_framework.response import Response
from .models import Users , Files
import rest_framework.status
from .utils import encrypt_password
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .forms import LoginForm
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .forms import RegisterForm , FilesForm 
from rest_framework.parsers import FileUploadParser , MultiPartParser , FormParser
from rest_framework.viewsets import ModelViewSet


class UserViews(APIView):
    
    
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
        try:
            print(request.POST)
            loginform = LoginForm(request.POST)

            if loginform.is_valid():
                
                email = loginform.cleaned_data["email"]
                password = loginform.cleaned_data["password"]
                user = Users.objects.get(email = email)
                if user and user.is_active and user.check_password(password):
                    
                    token = RefreshToken.for_user(user = user)
                    response = {
                        "token" : str(token.access_token),
                        "user_id" : user.id,
                        "role" : user.is_staff or 0
                    }
                    
                    return Response(response , status=rest_framework.status.HTTP_202_ACCEPTED)
                
                else:
                    response = {"message" : "Invalid Credentials"}
                    return Response(response , status=rest_framework.status.HTTP_401_UNAUTHORIZED)
                    
                    
        except Users.DoesNotExist:
            response = {"message" : "User does not exist"}
            return Response(response , status=rest_framework.status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            response = {"message" : str(e)}
            return Response(response,status=rest_framework.status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class RegsiterView(APIView):
    
    
    def post(self,request):
        
        try:
            registerform = RegisterForm(request.POST)
            
            if registerform.is_valid():
                
                user_data = registerform.cleaned_data
                serialised_data = UserSerializer(data = user_data)
                if serialised_data.is_valid():
                    
                    created_user = serialised_data.create(serialised_data.data)
                    token = RefreshToken.for_user(created_user)
                    response_data = {
                        "token" : str(token.access_token),
                        "user_id" : created_user.id,
                        "role" : 0
                    }
                    
                    return Response(response_data , status=rest_framework.status.HTTP_201_CREATED)
                
                else:
                    return Response(serialised_data.errors , status=rest_framework.status.HTTP_401_UNAUTHORIZED)
            
            else :
                return Response(registerform.errors , status=rest_framework.status.HTTP_401_UNAUTHORIZED)
                          
        except Exception as e:
            response = {"message" : str(e)}
            return Response(response , status=rest_framework.status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class FileViews(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser,FormParser)
    
    def post(self,request):
        try:
            file = request.FILES.get("file")
            user_id = request.POST.get("user_id")
            
            print(file)
            print(user_id)
            
            if not file or not user_id:
                return Response({"message": "Both 'file' and 'user_id' are required."}, status=rest_framework.status.HTTP_400_BAD_REQUEST)
            data = {"file_store": file, "file_name": file.name,"user_id": user_id}
            print(data)
            file_form = FileUploadSerialiser(data = data)
            if file_form.is_valid():
                file_form.save()
                response = {"message" : "File is uploaded"}
                return Response(response , status = rest_framework.status.HTTP_201_CREATED)
        
            else:
                print(file_form.errors)
                response = {"message" : file_form.errors}
                return Response(response , status=rest_framework.status.HTTP_400_BAD_REQUEST)
        
        
        except Exception as e:
            print(e)
            response = {"message" : str(e)}
            return Response(response , status = rest_framework.status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def get(self,request,pk):
        try:
            user_id = pk
            if user_id:
                file_list = Files.objects.filter(user_id = user_id)
                serialized_file_list = FileUploadSerialiser(file_list,many=True)
                if not file_list:
                    response = {"message" : "No file found"}
                    return  Response(response , status=rest_framework.status.HTTP_404_NOT_FOUND)

                file_name = [item.get("file_name",[]) for item in serialized_file_list.data]
                response = {"file_names" : file_name}
                return Response(response  , status=rest_framework.status.HTTP_202_ACCEPTED)
    

        except Exception as e:
            response = {"message" : str(e)}
            return Response(response,status=rest_framework.status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self , request):
        try:
            file_name = request.POST.get("file_name",None) or request.body.get("file_name" , None)
            if not file_name:
                response = {"message" : "Please enter a file_name"}
                return Response(response ,status=rest_framework.status.HTTP_400_BAD_REQUEST)
            
            file_found = Files.objects.get(file_name=file_name)
            if not file_found:
                response  = {"message" : "File not found with the file name"}
                return Response(response , status=rest_framework.status.HTTP_404_NOT_FOUND)
            
            file_found.delete()
            response = {"message" : "File deleted successfully"}
            return Response(response , status=rest_framework.status.HTTP_200_OK)
        except Exception as e:
            response = {"message" : str(e)}
            return Response(response, status=rest_framework.status.HTTP_500_INTERNAL_SERVER_ERROR)