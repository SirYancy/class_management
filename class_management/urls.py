"""
URL Patterns for root

Included are:
* / -redirects to attendance/
* attendance/ - Currently just attendance sign-in sheet
* admin/ - Site admin page (requires login)
* api-token-path/ - Get auth token (requires proper credential headers)
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponseRedirect

from rest_framework.authtoken import views

urlpatterns = [
    url(r'^$', lambda r: HttpResponseRedirect('instructor/')),
    url(r'^instructor/', include('attendance.urls', namespace='instructor')),
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^instructor/', include('instructor.urls', namespace='instructor')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += [
    url(r'^api-token-auth/', views.obtain_auth_token),
]
