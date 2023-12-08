from django.shortcuts import render,redirect, get_object_or_404
from hotel_app import auth
import json
from django.http import JsonResponse
from hotel_app.models import Room, RoomBooking, User
from django.http import HttpResponseForbidden
from .forms import RoomForm
from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models import Q

def format_date(date):
    return date.strftime("%Y/%m/%d")
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
    adults = request.GET.get('adults')
    children = request.GET.get('children')
    room_count = request.GET.get('rooms')
    start_date = request.GET.get('startDate')
    end_date = request.GET.get('endDate')
    print(start_date)
    print(end_date)
    if adults is not None:
        rooms = rooms.filter(adults__gte=adults)
    if children is not None:
        rooms = rooms.filter(children__gte=children)
    if room_count is not None:
        rooms = rooms.filter(rooms__gte=room_count)
    if start_date is not None and end_date is not None:
        booked_rooms = RoomBooking.objects.filter(
            Q(start_date__lte=start_date, end_date__gte=start_date) |
            Q(start_date__lte=end_date, end_date__gte=end_date) |
            Q(start_date__gte=start_date, end_date__lte=end_date)
        ).values_list('room_id', flat=True)

        rooms = rooms.exclude(room_id__in=booked_rooms)

        if start_date > end_date:
            rooms = []
        print(rooms)
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
def book(request):
    if request.method == 'POST':
        user_json = request.session.get('user', '{}')
        user_data = json.loads(user_json)
        user_id = user_data.get('id')
        json_data = json.loads(request.body.decode('utf-8'))
        room_id = json_data.get('room_id')
        date_str = json_data.get('date')
        start_date = datetime.strptime(date_str, "%Y/%m/%d")
        room = Room.objects.get(room_id=room_id)
        user = User.objects.get(id=user_id)
        room_booking = RoomBooking.objects.create(
            room_id=room.room_id,
            user_id=user.id,
            start_date=start_date.replace(hour=13, minute=0, second=0, microsecond=0),
            end_date=start_date + start_date.replace(hour=13, minute=0, second=0, microsecond=0) + timedelta(days=1)
        )
        room_booking.save()
        return JsonResponse({'status': 'Success'})
    elif request.method == 'DELETE':
        json_data = json.loads(request.body.decode('utf-8'))
        booking_id = json_data.get('booking_id')
        room_booking = get_object_or_404(RoomBooking, booking_id=booking_id)
        room_booking.delete()
        return JsonResponse({'status': 'Success'})
    return HttpResponseForbidden("You do not have permission to access this resource.")
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
    bookings = RoomBooking.objects.filter(room=room_id)
    current_date = datetime.now().date()
    next_month = [current_date + timedelta(days=i) for i in range(30)]
    valid_dates = [
        format_date(date) for date in next_month
        if not any(
            booking.start_date.date() <= date <= booking.end_date.date() for booking in bookings
        )
    ]
    return render(request, 'details.html', {
        'user_id': user_id,
        'user_first_name': user_first_name,
        'user_last_name': user_last_name,
        'user_email': user_email,
        'user_phone': user_phone,
        "role": role,
        "room": rooms[0],
        "valid_dates": valid_dates
    })
def receive(request):
    user_json = request.session.get('user', '{}')
    user_data = json.loads(user_json)
    user_id = user_data.get('id')
    user_first_name = user_data.get('first_name')
    user_last_name = user_data.get('last_name')
    user_email = user_data.get('email')
    user_phone = user_data.get('phone')
    role = user_data.get('role')
    bookings = RoomBooking.objects.filter()
    return render(request, 'receive.html', {
        'user_id': user_id,
        'user_first_name': user_first_name,
        'user_last_name': user_last_name,
        'user_email': user_email,
        'user_phone': user_phone,
        "role": role,
        "bookings": bookings
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