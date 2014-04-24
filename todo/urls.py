# -*-coding: utf-8 -*-
#!/usr/bin/env python
from __future__ import unicode_literals

from django.conf.urls import patterns, url

from todo import views

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns(
    '',
    url(r'^$', views.todolist, name='todo'),
    url(r'^addtodo/$', views.addTodo, name='add'),
    url(r'^todofinish/(?P<id>\d+)/$', views.todofinish, name='finish'),
    url(r'^todobackout/(?P<id>\d+)/$', views.todoback,  name='backout'),
    url(r'^updatetodo/(?P<id>\d+)/$', views.updatetodo, name='update'),
    url(r'^tododelete/(?P<id>\d+)/$', views.tododelete, name='delete'),

)
