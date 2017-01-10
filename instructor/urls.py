from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.InstructorIndexView.as_view(), name='instructor_index'),
    url(r'^create_class/$', views.CreateClassView.as_view(), name='instructor_create_class'),
]
