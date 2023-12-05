from django.shortcuts import render,redirect
from hotel_app import auth
from django.contrib.auth import logout

def index(request):
    user = request.user
    # user_id = user.id
    # username = user.username
    # print(username)
    return render(request, 'index.html')
def login(request):
    if request.method == 'POST':
        return auth.login_user(request)
    return render(request, 'login.html')
def logout_user(request):
    logout(request)
    return redirect('index')
def about(request):
    return render(request, 'about.html')
def product(request):
    return render(request, 'product.html')
def room(request):
    return render(request, 'room.html')
def register(request):
    if request.method == 'POST':
        return auth.create_user(request)
    return render(request, 'register.html')
def uilchilgee(request):
    return render(request, 'uilchilgee.html')
