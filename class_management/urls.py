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


urlpatterns = [
    url(r'^$', lambda r: HttpResponseRedirect('attendance/')),
    url(r'^attendance/', include('attendance.urls', namespace='attendance')),
    url(r'^admin/', admin.site.urls),
]

from rest_framework.authtoken import views

urlpatterns += [
    url(r'^api-token-auth/', views.obtain_auth_token),
]
