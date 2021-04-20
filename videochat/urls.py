from django.urls import re_path, path
from . import views

urlpatterns = [
    path('token', views.token, name='token'),
    path('', views.landing, name='landing'),
    #re_path(r'rooms/(?P<slug>[-\w]+)/$', views.room_detail, name="room_detail"),
]