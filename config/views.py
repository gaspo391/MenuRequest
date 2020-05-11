from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

User = get_user_model()

# Create your views here.
def indexfunc(request):
  return render(request, 'index.html')

def signupfunc(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    try:
      User.objects.get(username=username)
      return render(request, "accounts/signup.html", {"error":"このユーザーは登録されています"})
    except:
      user = User.objects.create_user(username, '', password)
      # return render(request, 'menu/menu.html')
      return redirect('menuapp:menu')
  return render(request, 'accounts/signup.html')

def loginfunc(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('menuapp:menu')
    else:
        return redirect('login')
  return render(request, 'accounts/login.html')

def logoutfunc(request):
    logout(request)
    return redirect('index')