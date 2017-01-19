from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ClassView.as_view(), name='choose_class'),
    url(r'^signin/$', views.SignInView.as_view(), name='signin'),
    url(r'^verify/$', views.verify, name='verify'),
    url(r'^student_detail/(?P<pk>[0-9]+)/(?P<class>[0-9]+)$', views.StudentDetailView.as_view(), name='student_detail'),
]
