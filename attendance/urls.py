from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ClassView.as_view(), name='choose_class'),
    url(r'^signin/$', views.SignInView.as_view(), name='signin'),
    url(r'^verify/$', views.verify, name='verify'),
]
