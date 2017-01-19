from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from attendance.models import Class, Student, Session


class CreateClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['semester', 'year', 'class_id', 'name']


class EnrollStudentsForm(forms.ModelForm):
    class Meta:
        model = Class
        exclude = ['semester', 'year', 'class_id', 'name']

    def __init__(self, *args, **kwargs):
        super(EnrollStudentsForm, self).__init__(*args, **kwargs)
        self.fields["enrolled_students"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["enrolled_students"].help_text = ""
        self.fields["enrolled_students"].queryset = Student.objects.all()


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'student_id']


class CreateSessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['date', 'session_class', 'password']
        widgets = {
            'date': AdminDateWidget(attrs={'class': 'datepicker', }),
        }


# class UpdateSessionForm(forms.Form):
#     students_present = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)
#
#     def __init__(self, session, *args, **kwargs):
#         super(UpdateSessionForm, self).__init__(*args, **kwargs)
#         c = session.session_class
#         self.fields['students_present'].queryset = c.enrolled_students.all()
#         # self.fields['students_present'].initial = [session.students_present]


class UpdateSessionForm(forms.ModelForm):
    class Meta:
        model = Session
        exclude = ['date', 'password', 'is_open', 'session_class']

    def __init__(self, session, *args, **kwargs):
        super(UpdateSessionForm, self).__init__(*args, **kwargs)
        c = session.session_class
        self.fields['students_present'].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields['students_present'].helpt_text = ""
        self.fields['students_present'].queryset = c.enrolled_students.all()
        self.fields['students_present'].initial = [session.students_present]
