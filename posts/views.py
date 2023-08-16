from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(http_method_names=["GET", "POST"])
def home_page(request):
    response = {'Message': 'hello world'}
    return Response(data=response, status=status.HTTP_200_OK)
