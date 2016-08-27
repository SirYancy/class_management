from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$', views.SignInView.as_view(), name='signin'),
    url(r'^verify/$', views.verify, name='verify'),
]