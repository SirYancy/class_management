from django import forms


class SignInForm(forms.Form):
    student_id = forms.CharField(label='Student ID', max_length=6)
    today_password = forms.CharField(label="Today's Password", max_length=20, widget=forms.PasswordInput)
