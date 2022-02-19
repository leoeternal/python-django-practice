from django.urls import path
from . import views

urlpatterns=[
  path('login/',views.loginPage,name="login"),
  path('register/',views.registerPage,name="register"),
  path('logout/',views.logoutUser,name="logout"),
  path('',views.home,name="home"),
  path('room/<str:pk>/',views.room,name="room"),
  path('create-room/',views.createRoom,name="create-room"),
  path('edit-room/<str:pk>/',views.editRoom,name="edit-room"),
  path('delete-room/<str:pk>/',views.deleteRoom,name="delete-room"),
  path('delete-message/<str:pk>/',views.deleteMessage,name="delete-message")
]