from rest_framework import serializers


from apps.user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class UserSerializerList(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']
