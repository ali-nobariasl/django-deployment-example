from django.conf.urls import url
from basic_app import views


urlpatterns = [
    url(r'^register/$', views.register, name='register'),
]
