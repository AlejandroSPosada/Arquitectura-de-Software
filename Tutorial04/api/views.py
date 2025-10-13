from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .serializers import ToDoSerializer, ToDoToggleCompleteSerializer
from todo.models import ToDo
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

class ToDoListCreate(generics.ListCreateAPIView):
    # ListAPIView requirestwo mandatory attributes, serializer_class and queryset
    # We specify TodoSerializer which we have earlier implemented
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ToDo.objects.filter(user=user).order_by('-created')

    def perform_create(self, serializer):
        # serializer holds a django model
        serializer.save(user=self.request.user)

class ToDoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # user can only update, delete own posts
        return ToDo.objects.filter(user=user)
    
class ToDoToggleComplete(generics.UpdateAPIView):
    serializer_class = ToDoToggleCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return ToDo.objects.filter(user=user)
    def perform_update(self,serializer):
        serializer.instance.completed=not(serializer.instance.completed)
        serializer.save()

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import IntegrityError
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)  # data is a dictionary
            user = User.objects.create_user(
                username=data['username'], 
                password=data['password']
            )
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token.key)}, status=201)
        except IntegrityError:
            return JsonResponse(
                {'error': 'username taken. choose another username'},
                status=400
            )
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(
            request,
            username=data['username'], 
            password=data['password']
        )
        if user is None:
            return JsonResponse(
                {'error': 'unable to login. check username and password'}, 
                status=400
            )
        else:  # return user token
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:  # if token not in db, create a new one
                token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token.key)}, status=200)
    return JsonResponse({'error': 'Method not allowed'}, status=405)