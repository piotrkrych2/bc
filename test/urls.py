"""test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from test.bc.views import NotificationPost, NotificationEmail, NotificationDetail, NotificationHistory

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^$', NotificationPost.as_view()),
    url(r'^my-notifications/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', NotificationEmail.as_view(),
        name='notification-email'),
    url(r'^notifications/(?P<pk>[0-9]+)/$', NotificationDetail.as_view(), name='notification-detail'),
    url(r'^history/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', NotificationHistory.as_view(),
        name='notification-history'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
