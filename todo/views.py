# -*-coding: utf-8 -*-
#!/usr/bin/env python
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.http import Http404
from models import Todo


def todolist(request):
    todolist = Todo.objects.filter(flag=1)
    finishtodos = Todo.objects.filter(flag=0)
    return render_to_response('simpleTodo.html',
        {'todolist': todolist, 'finishtodos': finishtodos},
        context_instance=RequestContext(request))


def todofinish(request, id=''):
    todo = Todo.objects.get(id=id)
    if todo.flag == '1':
        todo.flag = '0'
        todo.save()
        return HttpResponseRedirect('/todos/')
    todolist = Todo.objects.filter(flag=1)
    return render_to_response('simpleTodo.html', {'todolist': todolist},
        context_instance=RequestContext(request))


def todoback(request, id=''):
    todo = Todo.objects.get(id=id)
    if todo.flag == '0':
        todo.flag = '1'
        todo.save()
        return HttpResponseRedirect('/todos/')
    todolist = Todo.objects.filter(flag=1)
    return render_to_response('simpleTodo.html', {'todolist': todolist},
        context_instance=RequestContext(request))


def tododelete(request, id=''):
    try:
        todo = Todo.objects.get(id=id)
    except Exception:
        raise Http404
    if todo:
        todo.delete()
        return HttpResponseRedirect('/todos/')
    todolist = Todo.objects.filter(flag=1)
    return render_to_response('simpleTodo.html', {'todolist': todolist},
        context_instance=RequestContext(request))


def addTodo(request):
    if request.method == 'POST':
        atodo = request.POST['todo']
        priority = request.POST['priority']
        user = User.objects.get(id='1')
        todo = Todo(user=user, todo=atodo, priority=priority, flag='1')
        todo.save()
        todolist = Todo.objects.filter(flag='1')
        finishtodos = Todo.objects.filter(flag=0)
        return render_to_response('showtodo.html',
            {'todolist': todolist, 'finishtodos': finishtodos},
            context_instance=RequestContext(request))
    else:
        todolist = Todo.objects.filter(flag=1)
        finishtodos = Todo.objects.filter(flag=0)
        return render_to_response('simpleTodo.html',
            {'todolist': todolist, 'finishtodos': finishtodos})


def updatetodo(request, id=''):
    if request.method == 'POST':
        try:
            todo = Todo.objects.get(id=id)
        except Exception:
            return HttpResponseRedirect('/todos/')
        atodo = request.POST['todo']
        priority = request.POST['priority']
        todo.todo = atodo
        todo.priority = priority
        todo.save()
        return HttpResponseRedirect('/todos/')
    else:
        try:
            todo = Todo.objects.get(id=id)
        except Exception:
            raise Http404
        return render_to_response('updatatodo.html', {'todo': todo},
            context_instance=RequestContext(request))
