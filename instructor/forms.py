from django.forms import ModelForm

from attendance.models import Class


class CreateClassForm(ModelForm):
    class Meta:
        model = Class
        fields = ['semester', 'year', 'class_id', 'name']

