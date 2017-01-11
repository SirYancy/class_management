from django.conf.urls import url
from django.http import HttpResponseRedirect

from . import views

urlpatterns = [
    url(r'^$', lambda r: HttpResponseRedirect('instructor/login')),
    url(r'^index/$', views.InstructorIndexView.as_view(), name='instructor_index'),
    url(r'^create_class/$', views.CreateClassView.as_view(), name='instructor_create_class'),
    url(r'^class_detail/(?P<pk>[0-9]+)$', views.ClassDetailView.as_view(), name='class_detail'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/&', views.user_logout, name='logout'),
]
