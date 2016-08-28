from django.shortcuts import render_to_response
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date

from .models import Class, Student, Session
from .forms import SignInForm


class SignInView(FormView):
    template_name = 'attendance/signin.html'
    form_class = SignInForm


def verify(request):
    if request.GET:
        today = date.today()
        student = Student.objects.get(student_id=request.GET.get('student_id'))
        current_class = Class.objects.get(class_id=request.GET.get('class_id'))
        class_id = current_class.id
        sessions = Session.objects.filter(session_class=class_id).filter(date__exact=today)
        s = sessions[0]

        if student.enrolled_class == current_class and request.GET.get('today_password') == s.password:
            s.students_present.add(student)
            s.save()
            return HttpResponse("Thank you, %s" % student.first_name)

        return HttpResponse("Password, Student ID, or Class incorrect.")
