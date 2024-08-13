from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['POST'])
def singup(request):
    return Response("singup")

@api_view(['POST'])
def login(request):
    return Response("login")