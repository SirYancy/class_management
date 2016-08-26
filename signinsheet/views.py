from django.shortcuts import render_to_response
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.utils import timezone

from .models import Class, Student, Session


class SignInView(generic.TemplateView):
    template_name = 'signinsheet/signin.html'


#def verify_sign(request):
