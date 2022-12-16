from rest_framework import serializers
from django.contrib.auth.models import User

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = ('name', 'employee_id')
        fields = '__all__'
