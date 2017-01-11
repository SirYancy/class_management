from django.forms import ModelForm

from attendance.models import Class, Student


class CreateClassForm(ModelForm):
    class Meta:
        model = Class
        fields = ['semester', 'year', 'class_id', 'name']


class CreateStudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'student_id']
