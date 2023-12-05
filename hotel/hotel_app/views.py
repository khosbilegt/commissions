from django.shortcuts import render,redirect
from hotel_app import auth
from django.contrib import sessions
import json

def index(request):
    user_json = request.session.get('user', '{}')
    user_data = json.loads(user_json)

    # Perform actions based on user information
    user_id = user_data.get('id')
    user_first_name = user_data.get('first_name')
    user_last_name = user_data.get('last_name')
    user_email = user_data.get('email')
    user_phone = user_data.get('phone')
    return render(request, 'index.html', {
        'user_id': user_id,
        'user_first_name': user_first_name,
        'user_last_name': user_last_name,
        'user_email': user_email,
        'user_phone': user_phone,
    })
def login(request):
    print(request)
    if request.method == 'POST':
        return auth.login_user(request)
    return render(request, 'login.html')
def logout(request):
    return auth.logout_user(request)
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
