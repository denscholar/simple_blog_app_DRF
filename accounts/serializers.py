from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token


class SignUpSerializer(serializers.ModelSerializer):
    # Add some validation
    email = serializers.CharField(max_length=80)
    username = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ("email", "username", "password")

    # creat a validation to check if user exist in the database
    def validate(self, data):
        email_exist = CustomUser.objects.filter(email=data["email"])
        if email_exist.exists():
            raise serializers.ValidationError({"errors": "Email already exists"})
        return data
    
    """You will need to hash the passowrd and to do that, you will need to overide the create method. The create method is one that will run each time we call the .save method. so we are going to overide that and dictate how we will save the data in the database."""

    def create(self, validated_data):
        passwords = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(passwords)
        
        # Saves the user to the database
        user.save() 

        # This creates a token for this specific user that signs up
        Token.objects.create(user=user)
        return user
