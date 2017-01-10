from django.http import HttpResponse
from django.views import generic

from attendance.models import Class
from .forms import CreateClassForm


class InstructorIndexView(generic.ListView):
    template_name = "instructor/index.html"
    context_object_name = "class_list"

    def get_queryset(self):
        classes = None
        if self.request.user.is_authenticated():
            classes = Class.objects.all()
        return classes


class CreateClassView(generic.CreateView):
    template_name = "instructor/create_class.html"
    form_class = CreateClassForm
    success_url = '/instructor/'

    def form_invalid(self, form):
        return HttpResponse("Form is invalid...redo it.")

