# users/views.py

from django.contrib.auth import get_user_model, hashers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
import json

User = get_user_model()

@csrf_exempt
@require_POST
def sign_up(request):
    try:
        data = json.loads(request.body)
        username = data['username']
        email = data['email']
        password1 = data['password1']
        password2 = data['password2']
        is_employer = data.get('is_employer', False)
        is_employee = data.get('is_employee', False)

        if password1 != password2:
            return JsonResponse({'error': 'Passwords do not match'}, status=400)

        hashed_password = hashers.make_password(password1)

        user = User.objects.create(
            username=username,
            email=email,
            password=hashed_password,
            is_employer=is_employer,
            is_employee=is_employee
        )

        return JsonResponse({'message': 'User registered successfully'}, status=201)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
@csrf_exempt
@require_POST
def sign_in(request):
    try:
        data = json.loads(request.body)
        username = data['username']
        password = data['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({'token': token.key}, status=200)
        else:
            return JsonResponse({'error': 'Invalid login credentials'}, status=401)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)