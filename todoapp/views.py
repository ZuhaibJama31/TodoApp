from django.shortcuts import render
from django.views.generic import ListView ,CreateView,DeleteView
from django.urls import reverse_lazy
from .models import MakeList
# Create your views here.

class TodoListView(ListView):
    model = MakeList
    template_name = 'todoapp/makelist_list.html'


class TodoCreateView(CreateView):
    model = MakeList
    template_name = 'todoapp/makelist_form.html'
    fields = "__all__"
    success_url = reverse_lazy('todo-list')


class TodoDeleteView(DeleteView):
    model = MakeList
    template_name = 'todoapp/makelist_delete.html'
    fields = []
    success_url = reverse_lazy('todo-list')
