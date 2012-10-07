#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from simpleToDo.models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('user', 'todo', 'priority', 'flag', 'pubtime')
    list_filter = ('pubtime',)
    ordering = ('-pubtime',)


admin.site.register(Todo, TodoAdmin)  
