from rest_framework import serializers 


class LoginSerializer(serializers.Serializer) : 
    username = serializers.CharField(
        max_length=50, 
        style={'placeholder': 'Username'}
    )

    password = serializers.CharField(
        max_length=50, 
        style={
            'placeholder': 'Password', 
            'input_type': 'password'}
    )