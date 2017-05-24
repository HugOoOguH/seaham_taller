from django.conf.urls import url
from . import views

urlpatterns=[
	url('^home/$', views.Home.as_view(), name="home"),
]