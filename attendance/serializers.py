from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from attendance.models import Student, Class, Session


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key',)


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ('class_id', 'name', 'year', 'semester',)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('last_name', 'first_name', 'student_id', 'enrolled_class')


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('date', 'password', 'session_class', 'students_present', 'is_open')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name')
