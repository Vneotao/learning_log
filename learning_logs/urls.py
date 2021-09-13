from django.db import router
from django.urls import path
from django.urls.conf import path, re_path
from django.views.generic import TemplateView
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('topics/', views.topics, name='topics'),
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
    re_path(r'^delete_entry/(?P<entry_id>\d+)/$', views.delete_entry, name='delete_entry'),
]