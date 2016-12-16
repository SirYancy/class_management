from django.conf.urls import url

from . import views

# Rest Interface
urlpatterns = [
    url(r'^classes/$',
        views.ClassList.as_view(),
        name='rest_class'),
    url(r'^students/(?P<class_key>[0-9]+)/$',
        views.StudentList.as_view(),
        name='rest_students'),
    url(r'^sessions/$',
        views.SessionList.as_view(),
        name='rest_session'),
    url(r'^sessions/(?P<class_key>[0-9]+)/$',
        views.SessionList.as_view(),
        name='rest_sessions_class'),
    url(r'^sessions/(?P<pk>[0-9]+)/$',
        views.SessionDetail.as_view(),
        name='rest_session_detail'),
    url(r'^sessions_update/(?P<pk>[0-9]+)/$',
        views.SessionDetail.as_view(),
        name='rest_session_update'),
    url(r'^current_user/$',
        views.CurrentUser.as_view(),
        name='rest_current_user'),
]
