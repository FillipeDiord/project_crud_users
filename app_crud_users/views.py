from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import User

def listUsers(request):
  users = {'users': User.objects.all()}
  return render(request, 'users/list_users.html', users)

def addUsers(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    age = request.POST.get('age')

    if not name or not age:
      messages.error(request, "Todos os campos são obrigatórios.")
      return render(request, 'users/add_users.html', {'users': User.objects.all()})

    try:
      age = int(age)
      if age < 0:
        raise ValidationError("A idade não pode ser negativa.")
            
      new_user = User(name=name, age=age)
      new_user.full_clean()
      new_user.save()

      messages.success(request, "Usuário adicionado com sucesso!")
      return redirect('list_users')
    except ValueError:
      messages.error(request, "A idade precisa ser um número válido.")
      return render(request, 'users/add_users.html', {'users': User.objects.all()})
    except ValidationError as e:
      messages.error(request, e.message)
      return render(request, 'users/add_users.html', {'users': User.objects.all()})

  return render(request, 'users/add_users.html', {'users': User.objects.all()})

def updateUser(request, user_id):
  user = get_object_or_404(User, id_user=user_id)

  if request.method == 'POST':
    name = request.POST.get('name', user.name)
    age = request.POST.get('age', user.age)

    try:
      age = int(age)
      if age < 0:
        raise ValidationError("A idade não pode ser negativa.")
            
      user.name = name
      user.age = age
      user.full_clean()
      user.save()

      messages.success(request, "Usuário atualizado com sucesso!")
      return redirect('list_users')
    except ValueError:
      messages.error(request, "A idade precisa ser um número válido.")
      return render(request, 'users/update_user.html', {'user': user})
    except ValidationError as e:
      messages.error(request, e.message)
      return render(request, 'users/update_user.html', {'user': user})

  return render(request, 'users/update_user.html', {'user': user})

def deleteUser(request, user_id):
  try:
    user = User.objects.get(id_user=user_id)
    if request.method == 'POST':
      user.delete()
            
      messages.success(request, "Usuário deletado com sucesso!")
      return redirect('list_users')
  except User.DoesNotExist:
    messages.error(request, "Usuário não encontrado.")
    return redirect('list_users')

  return redirect('list_users')
