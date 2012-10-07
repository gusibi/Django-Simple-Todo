#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import *

urlpatterns = patterns(('simpleToDo.views'),
    url(r'^$', 'todolist', name='todo'),
    url(r'^addtodo/$', 'addTodo', name='add'),
    url(r'^todofinish/(?P<id>\d+)/$', 'todofinish', name='finish'),
    url(r'^todobackout/(?P<id>\d+)/$', 'todoback',  name='backout'),
    url(r'^updatetodo/(?P<id>\d+)/$', 'updatetodo', name='update'),
    url(r'^tododelete/(?P<id>\d+)/$', 'tododelete', name='delete'),
)