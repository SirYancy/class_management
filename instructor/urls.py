from django.conf.urls import url
from django.http import HttpResponseRedirect

from . import views

urlpatterns = [
    url(r'^$', lambda r: HttpResponseRedirect('instructor/login')),
    url(r'^index/$', views.InstructorIndexView.as_view(), name='instructor_index'),
    url(r'^student_list/$', views.StudentListView.as_view(), name='instructor_student_list'),
    url(r'^create_class/$', views.CreateClassView.as_view(), name='instructor_create_class'),
    url(r'^create_student/$', views.CreateStudentView.as_view(), name='instructor_create_student'),
    url(r'^class_detail/(?P<pk>[0-9]+)$', views.ClassDetailView.as_view(), name='class_detail'),
    url(r'^create_session/(?P<pk>[0-9]+)$', views.CreateSessionView.as_view(), name='instructor_create_session'),
    url(r'^enroll_students/(?P<pk>[0-9]+)$', views.EnrollStudentsView.as_view(), name='enroll_students'),
    url(r'^close_sessions/(?P<class_id>[0-9]+)$', views.close_sessions, name='close_sessions'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/&', views.user_logout, name='logout'),
]
