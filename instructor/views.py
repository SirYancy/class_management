from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from attendance.models import Class, Session, Student
from .forms import CreateClassForm, CreateStudentForm


class InstructorIndexView(generic.ListView):
    template_name = "instructor/index.html"
    context_object_name = "class_list"

    def get_queryset(self):
        classes = None
        if self.request.user.is_authenticated():
            classes = Class.objects.all()
        return classes


class StudentListView(generic.ListView):
    template_name = "instructor/student_list.html"
    context_object_name = 'students'

    def get_queryset(self):
        students = None
        if self.request.user.is_authenticated():
            students = Student.objects.all().order_by('last_name')
        return students


class CreateClassView(generic.CreateView):
    template_name = "instructor/create_class.html"
    form_class = CreateClassForm
    success_url = '/instructor/index/'

    def form_invalid(self, form):
        return HttpResponse("Form is invalid...redo it.")


class CreateStudentView(generic.CreateView):
    template_name = "instructor/create_student.html"
    form_class = CreateStudentForm
    success_url = '/instructor/create_student'

    def form_invalid(self, form):
        return HttpResponse("Form is invalid")


class ClassDetailView(generic.DetailView):
    template_name = "instructor/class_detail.html"
    model = Class
    context_object_name = 'class_detail'

    def get_context_data(self, **kwargs):
        context = super(ClassDetailView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            my_class = self.get_object()
            my_sessions = Session.objects.filter(session_class=my_class).order_by('date')
            context['sessions'] = my_sessions
        return context


def user_login(request):
    """
    Login request view
    :param request:
    :return:
    """
    if request.user.is_authenticated():
        return HttpResponseRedirect('/instructor/index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/instructor/index/')
            else:
                return HttpResponse('Your account is disabled')
        else:
            print('Invalid Login')
            return HttpResponse('Invalid login details')
    else:
        return render(request, 'instructor/login.html')


@login_required
def user_logout(request):
    """
    Logs current client out
    :param request:
    :return:
    """
    logout(request)
    return HttpResponseRedirect('/attendance/')
