import csv

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from attendance.models import Class, Session, Student
from .forms import CreateClassForm, CreateStudentForm, EnrollStudentsForm, CreateSessionForm, UpdateSessionForm


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

    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            my_classes = Class.objects.all()
            context['classes'] = my_classes
        return context


class CreateClassView(generic.CreateView):
    template_name = "instructor/create_class.html"
    form_class = CreateClassForm
    success_url = '/instructor/index/'

    def form_invalid(self, form):
        return HttpResponse("Form is invalid...redo it.")


@login_required
def create_session(request, pk):
    if request.method == 'POST':
        form = CreateSessionForm(request.POST)
        if form.is_valid():
            s = form.save()
            return HttpResponseRedirect('/instructor/class_detail/%i' % s.session_class.id)
    else:
        obj = Class.objects.get(id=pk)
        form = CreateSessionForm(initial={'session_class': obj.id})
        return render(request, "instructor/create_session.html", {"form": form})


class EnrollStudentsView(generic.UpdateView):
    template_name = 'instructor/enroll_students.html'
    form_class = EnrollStudentsForm
    success_url = '/instructor/index'

    def get_object(self, queryset=None):
        obj = Class.objects.get(id=self.kwargs['pk'])
        return obj


def update_session(request, pk):
    if request.method == 'POST':
        s = Session.objects.get(id=pk)
        c = s.session_class
        if 'students_present' in request.POST:
            s.students_present.clear()
            spid = request.POST.getlist('students_present')
            spid = list(map(int, spid))
            sp = Student.objects.filter(id__in=spid)
            for student in sp:
                s.students_present.add(student)
        else:
            s.students_present.clear()
        return HttpResponseRedirect('/instructor/class_detail/%i' % c.id)
    else:
        s = Session.objects.get(id=pk)
        form = UpdateSessionForm(s)
        ctx = {"form": form, "session": s}
        return render(request, "instructor/update_session.html", ctx)


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


def output_csv(request, class_id):
    """
    Outputs selected class to csv file
    :param class_id: id number of class
    :param request: request object
    :return: a csv file attached to http response
    """
    my_class = Class.objects.get(id=class_id)
    disp = 'attachment; filename="attendance_data_' + my_class.class_id + '.csv"'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = disp

    my_sessions = Session.objects.filter(session_class=my_class).order_by('date')
    my_students = my_class.enrolled_students.order_by('last_name', 'first_name')

    writer = csv.writer(response)
    title_row = [my_class.class_id + " " + my_class.name]
    writer.writerow(title_row)
    header_row = ["Name"]
    for session in my_sessions:
        header_row.append(session.date)
    writer.writerow(header_row)

    for student in my_students:
        data_row = [student.last_name + ", " + student.first_name]
        for session in my_sessions:
            if student.session_set.filter(id=session.id).exists():
                data_row.append("P")
            else:
                data_row.append("A")
        writer.writerow(data_row)

    return response


def close_sessions(request, class_id):
    """
    Closes all open sessions
    :param request:
    :return: HttpResponseRedirect
    """
    if not request.user.is_authenticated:
        HttpResponse("You are not allowed to do that")
    my_class = Class.objects.get(id=class_id)
    my_sessions = Session.objects.filter(session_class=my_class)
    for session in my_sessions:
        session.is_open = False
        session.save()
    return HttpResponseRedirect('/instructor/class_detail/%i' % my_class.id)


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
