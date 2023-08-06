from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView




def welcome(request):
    return HttpResponse("Hello, world!")