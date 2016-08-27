from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^signin/$', views.SignInView.as_view(), name='signin'),
]