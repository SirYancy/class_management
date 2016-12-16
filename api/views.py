from rest_framework import generics
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import SessionSerializer, ClassSerializer, StudentSerializer, UserSerializer
from attendance.models import Student, Class, Session


class StudentList(generics.ListAPIView):
    """
    List all Students
    """
    model = Student
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    ordering_fields = ('last_name',)
    ordering = ('last_name',)

    def get_queryset(self):
        key = self.kwargs['class_key']
        c = Class.objects.get(pk=key)
        return Student.objects.filter(enrolled_class=c).order_by('-last_name')


class SessionList(generics.ListCreateAPIView):
    """
    List all Sessions
    """
    model = Session
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = SessionSerializer
    ordering_fields = ('date',)
    ordering = ('date',)

    def get_queryset(self):
        key = self.kwargs['class_key']
        c = Class.objects.get(pk=key)
        return Session.objects.filter(session_class=c).order_by('-date')


class SessionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a Session
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = SessionSerializer
    queryset = Session.objects.all()


class ClassList(generics.ListCreateAPIView):
    """
    List all Classes
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class CurrentUser(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
