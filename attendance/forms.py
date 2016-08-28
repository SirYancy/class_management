from django import forms
from .models import Class


class SignInForm(forms.Form):
    student_id = forms.CharField(label='Student ID', max_length=6)
    today_password = forms.CharField(label="Today's Password", max_length=20, widget=forms.PasswordInput)


class ChooseClass(forms.Form):
    classes = forms.ModelChoiceField(queryset=Class.objects.all().order_by('name'))
