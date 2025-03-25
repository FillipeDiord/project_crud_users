from django.urls import path
from app_crud_users import views

urlpatterns = [
  path('', views.listUsers, name='list_users'),
  path('users/add_users', views.addUsers, name='add_users'),
  path('users/update/<int:user_id>/', views.updateUser, name='update_user'),
  path('users/delete/<int:user_id>/', views.deleteUser, name='delete_user'),
]
