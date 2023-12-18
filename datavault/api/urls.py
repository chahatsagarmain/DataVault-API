from django.urls import path 
from .views import (UserViews ,
                    LoginViews,
                    RegsiterView,
                    FileViews)
from rest_framework_simplejwt.views import (TokenObtainPairView 
                                            ,TokenRefreshView ,
                                            TokenVerifyView)

urlpatterns = [
    path('user/<int:id>/',UserViews.as_view(),name="get-user-by-id"),
    path('user/',UserViews.as_view(),name="create-user"),
    path('user/<int:id>',UserViews.as_view(),name="update-user-by-id"),
    path('user/<str:username>/',UserViews.as_view(),name="update-user-by-username"),
    path("user/<int:id>",UserViews.as_view(),name="delete-user"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('login/',LoginViews.as_view() , name="login-user"),
    path('register/',RegsiterView.as_view() , name="register-view"),
    path('file/',FileViews.as_view() , name = "upload-file"),
    path('file/<int:pk>',FileViews.as_view() , name='get-file-name')
]