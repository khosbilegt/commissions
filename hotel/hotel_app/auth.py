from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import json
from django.http import JsonResponse


def create_user(request):
     try:
          json_data = json.loads(request.body.decode('utf-8'))
          username = json_data.get('username', '')
          password = json_data.get('password', '')
          user = User.objects.create_user(username=username, password=password)
          if user is not None:
               return JsonResponse({'status': 'Success'})
          else:
               return JsonResponse({'status': 'Failure', 'message': 'Error creating user'})
     except json.JSONDecodeError:
          return JsonResponse({'status': 'Failure', 'message': 'Invalid JSON data'}, status=400)

def login_user(request):
    try:
        json_data = json.loads(request.body.decode('utf-8'))
        username = json_data.get('username', '')
        password = json_data.get('password', '')

        user = authenticate(request, username=username, password=password)
        if user is not None:
          login(request, user)
          return JsonResponse({"status": "Success"})
        return JsonResponse({"status": "Failed", "message": "User not found"})
    except User.DoesNotExist:
          return JsonResponse({"status": "Failed", "message": "User not found"})
