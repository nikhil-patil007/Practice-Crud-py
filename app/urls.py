from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('Add-User-Page/',views.add_user_page,name='adduserpage'),

    path('Add-user/',views.add_user,name='addusr'),

    path('Edit-User-Page/<int:pk>/',views.Edit_user_page,name='editpage'),
    path('Delete-User/<int:pk>/',views.deletuser,name="delete"),
    path('Update-User/<int:pk>/',views.updateusr,name="Update"),
]