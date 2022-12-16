from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import *

class UserAuthentication(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializers = self.serializer_class(data=request.data, context={'request': request})
        serializers.is_valid(raise_exception=True)
        user = serializers.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(token.key)

class UserList(APIView):
    def get(self, request):
        model = User.objects.all()
        serializers = UsersSerializer(model, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers = UsersSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    def get_user(self, username):
        try:
            model = User.objects.get(username=username)
            return model
        except User.DoesNotExist:
            return

    def get(self, request, username):
        if not self.get_user(username):
            return Response(f'User with {username} is Not Found in Database', status=status.HTTP_404_NOT_FOUND)
        serializers = UsersSerializer(self.get_user(username))
        return Response(serializers.data)

    def put(self, request, username):
        serializers = UsersSerializer(self.get_user(username), data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username):
        if not self.get_user(username):
            return Response(f'User with {username} is Not Found in Database', status=status.HTTP_404_NOT_FOUND)
        model = self.get_user(username)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
