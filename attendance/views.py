import csv
from datetime import date

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import FormView

from .forms import SignInForm, ChooseClassForm
from .models import Class, Student, Session


class ClassView(FormView):
    template_name = 'attendance/class.html'
    form_class = ChooseClassForm
    success_url = '/attendance/signin/'

    def form_valid(self, form):
        c = form.cleaned_data['classes']
        return HttpResponseRedirect(self.get_success_url() + "?class=" + c.class_id)


class SignInView(FormView):
    template_name = 'attendance/signin.html'
    form_class = SignInForm


def verify(request):
    """
    Verifies student id, class, and password. If it all matches up, the student is marked present for the day.
    :param request:
    :return:
    """
    if request.GET:
        today = date.today()
        student = None
        try:
            student = Student.objects.get(student_id=request.GET.get('student_id'))
        except Student.DoesNotExist:
            return HttpResponse("Student Does Not Exist")

        current_class = Class.objects.get(class_id=request.GET.get('class_id'))
        class_id = current_class.id
        sessions = Session.objects.filter(session_class=class_id).filter(date__exact=today)
        s = sessions[0]

        if s.students_present.filter(id=student.id).exists():
            return HttpResponse("<h3>You are already signed in</h3>")
        elif not s.is_open:
            return HttpResponse("This session is closed for signin.")
        elif student in current_class.enrolled_students.all() and request.GET.get('today_password') == s.password:
            s.students_present.add(student)
            s.save()
            return HttpResponse("<h3>Thank you, %s</h3>" % student.first_name)
        else:
            return HttpResponse("<h3>Password or Class incorrect</h3>")
