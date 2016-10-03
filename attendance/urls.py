from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ClassView.as_view(), name='choose_class'),
    url(r'^signin/$', views.SignInView.as_view(), name='signin'),
    url(r'^tabulate/(?P<pk>[0-9]+)$', views.TabulateView.as_view(), name='tabulate'),
    url(r'^classes/$', views.ClassIndexView.as_view(), name='classes'),
    url(r'^download/(?P<class_id>[0-9]+)$', views.output_csv, name='csv'),
    url(r'^verify/$', views.verify, name='verify'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
]

# Rest Interface
urlpatterns += [
    url(r'^rest_classes/$',
        views.ClassList.as_view(),
        name='rest_class'),
    url(r'^rest_students/(?P<class_key>[0-9]+)/$',
        views.StudentList.as_view(),
        name='rest_students'),
    url(r'^rest_sessions/$',
        views.SessionList.as_view(),
        name='rest_session'),
    url(r'^rest_sessions/(?P<class_key>[0-9]+)/$',
        views.SessionList.as_view(),
        name='rest_sessions_class'),
    url(r'^rest_sessions/(?P<pk>[0-9]+)/$',
        views.SessionDetail.as_view(),
        name='rest_session_detail'),
    url(r'^rest_current_user/$',
        views.CurrentUser.as_view(),
        name='rest_current_user'),
]
