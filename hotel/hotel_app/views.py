from django.shortcuts import render,redirect
from hotel_app import auth
from django.contrib import sessions
import json
from hotel_app.models import Room
from django.http import HttpResponseForbidden
from .forms import RoomForm

def login(request):
    if request.method == 'POST':
        return auth.login_user(request)
    return render(request, 'login.html')
def logout(request):
    return auth.logout_user(request)
def register(request):
    if request.method == 'POST':
        return auth.create_user(request)
    return render(request, 'register.html')
def index(request):
    user_json = request.session.get('user', '{}')
    user_data = json.loads(user_json)
    user_id = user_data.get('id')
    user_first_name = user_data.get('first_name')
    user_last_name = user_data.get('last_name')
    user_email = user_data.get('email')
    user_phone = user_data.get('phone')
    role = user_data.get('role')
    return render(request, 'index.html', {
        'user_id': user_id,
        'user_first_name': user_first_name,
        'user_last_name': user_last_name,
        'user_email': user_email,
        'user_phone': user_phone,
        "role": role
    })
def about(request):
    user_json = request.session.get('user', '{}')
    user_data = json.loads(user_json)
    user_id = user_data.get('id')
    user_first_name = user_data.get('first_name')
    user_last_name = user_data.get('last_name')
    user_email = user_data.get('email')
    user_phone = user_data.get('phone')
    role = user_data.get('role')
    return render(request, 'about.html', {
        'user_id': user_id,
        'user_first_name': user_first_name,
        'user_last_name': user_last_name,
        'user_email': user_email,
        'user_phone': user_phone,
        "role": role
    })
def product(request):
    user_json = request.session.get('user', '{}')
    user_data = json.loads(user_json)
    user_id = user_data.get('id')
    user_first_name = user_data.get('first_name')
    user_last_name = user_data.get('last_name')
    user_email = user_data.get('email')
    user_phone = user_data.get('phone')
    role = user_data.get('role')
    return render(request, 'product.html', {
        'user_id': user_id,
        'user_first_name': user_first_name,
        'user_last_name': user_last_name,
        'user_email': user_email,
        'user_phone': user_phone,
        "role": role
    })
def room(request):
    user_json = request.session.get('user', '{}')
    user_data = json.loads(user_json)
    user_id = user_data.get('id')
    user_first_name = user_data.get('first_name')
    user_last_name = user_data.get('last_name')
    user_email = user_data.get('email')
    user_phone = user_data.get('phone')
    role = user_data.get('role')
    rooms = Room.objects.all()
    return render(request, 'room.html', {
        'rooms': rooms,
        'user_id': user_id,
        'user_first_name': user_first_name,
        'user_last_name': user_last_name,
        'user_email': user_email,
        'user_phone': user_phone,
        "role": role
    })
def uilchilgee(request):
    user_json = request.session.get('user', '{}')
    user_data = json.loads(user_json)
    user_id = user_data.get('id')
    user_first_name = user_data.get('first_name')
    user_last_name = user_data.get('last_name')
    user_email = user_data.get('email')
    user_phone = user_data.get('phone')
    role = user_data.get('role')
    return render(request, 'uilchilgee.html', {
        'user_id': user_id,
        'user_first_name': user_first_name,
        'user_last_name': user_last_name,
        'user_email': user_email,
        'user_phone': user_phone,
        "role": role
    })
def order(request):
    # if request.method == 'POST':
    #     return auth.create_user(request)
    return render(request, 'register.html')
def details(request):
    user_json = request.session.get('user', '{}')
    user_data = json.loads(user_json)
    user_id = user_data.get('id')
    user_first_name = user_data.get('first_name')
    user_last_name = user_data.get('last_name')
    user_email = user_data.get('email')
    user_phone = user_data.get('phone')
    role = user_data.get('role')
    room_id = request.GET.get('id', '')
    rooms = Room.objects.filter(room_id=room_id)
    # if request.method == 'POST':
    #     return auth.create_user(request)
    return render(request, 'details.html', {
        'user_id': user_id,
        'user_first_name': user_first_name,
        'user_last_name': user_last_name,
        'user_email': user_email,
        'user_phone': user_phone,
        "role": role,
        "room": rooms[0]
    })
def manager(request):
    user_json = request.session.get('user', '{}')
    user_data = json.loads(user_json)
    user_id = user_data.get('id')
    user_first_name = user_data.get('first_name')
    user_last_name = user_data.get('last_name')
    user_email = user_data.get('email')
    user_phone = user_data.get('phone')
    role = user_data.get('role')
    if role == False:
        return HttpResponseForbidden("You do not have permission to access this resource.")
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RoomForm()
    return render(request, 'manager.html', {
        'user_id': user_id,
        'user_first_name': user_first_name,
        'user_last_name': user_last_name,
        'user_email': user_email,
        'user_phone': user_phone,
        "role": role,
        "form": form
    })