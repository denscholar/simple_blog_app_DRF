from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, generics
from .serializers import SignUpSerializer

# signup logic
class SignupView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()

            response = {
                "message": "user created successfully",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

