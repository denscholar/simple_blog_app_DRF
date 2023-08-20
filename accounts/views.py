from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, generics
from rest_framework.views import APIView
from .serializers import SignUpSerializer
from django.contrib.auth import authenticate


# signup logic
class SignupView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()

            response = {"message": "user created successfully", "data": serializer.data}
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)

        if user is not None:
            token = user.auth_token.key
            response = {
                "message": "user logged in successfully",
                "data": {"token": token},
            }
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(
            {"user": "user does not exist in our database"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def get(self, request: Request):
        content = {
            "user": str(request.user),
            "auth": str(request.auth),
        }
        return Response(data=content, status=status.HTTP_200_OK)
