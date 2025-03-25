from django.shortcuts import render, redirect
from .models import User

def listUsers(request):
  users = {'users': User.objects.all()}
  return render(request, 'users/list_users.html', users)

def addUsers(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    age = request.POST.get('age')

    if name and age:
      new_user = User()
      new_user.name = name
      new_user.age = age
      new_user.save()
    
    return redirect('/')
  
  users = {'users': User.objects.all()}
  return render(request, 'users/add_users.html', users)

def updateUser(request, user_id):
  user = User.objects.get(id_user=user_id)

  if request.method == 'POST':
    user.name = request.POST.get('name', user.name)
    user.age = request.POST.get('age', user.age)
    user.save()
    return redirect('/')
  
  return render(request, 'users/update_user.html', {'user': user})

def deleteUser(request, user_id):
  user = User.objects.get(id_user=user_id)

  if request.method == 'POST':
    user.delete()
    return redirect('/')
  
  return render(request, 'users/confirm_delete.html', {'user': user})
  
