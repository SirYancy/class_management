from django.shortcuts import render_to_response
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.utils import timezone

from .models import Class, Student, Session
from .forms import SignInForm


class SignInView(FormView):
    template_name = 'attendance/signin.html'
    form_class = SignInForm

    def form_valid(self, form):
        return HttpResponse("%s" % self.request.path)


def verify(request):
    if request.POST:
        return HttpResponse("%s" % request.path)
    if request.GET:
        return HttpResponse("%s" % request.path)
