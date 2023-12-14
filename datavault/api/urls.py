from django.urls import path 
from .views import UserViews

urlpatterns = [
    path('user/<int:id>/',UserViews.as_view(),name="get-user-by-id"),
    path('user/',UserViews.as_view(),name="create-user")
]