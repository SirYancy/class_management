from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import ModelForm, DateInput

from attendance.models import Class, Student, Session


class CreateClassForm(ModelForm):
    class Meta:
        model = Class
        fields = ['semester', 'year', 'class_id', 'name']


class EnrollStudentsForm(ModelForm):
    class Meta:
        model = Class
        exclude = ['semester', 'year', 'class_id', 'name']

    def __init__(self, *args, **kwargs):
        super(EnrollStudentsForm, self).__init__(*args, **kwargs)
        self.fields["enrolled_students"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["enrolled_students"].help_text = ""
        self.fields["enrolled_students"].queryset = Student.objects.all()


class CreateStudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'student_id']


class CreateSessionForm(ModelForm):
    class Meta:
        model = Session
        fields = ['date', 'session_class', 'password']
        widgets = {
            'date': AdminDateWidget(attrs={'class': 'datepicker',}),
        }
