from django.urls import path
from .views import TodoListView, TodoCreateView,TodoDeleteView

urlpatterns = [
    path('', TodoListView.as_view(), name="todo-list"),
    path('todo/create/', TodoCreateView.as_view(), name="todo-create"),
    path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name="todo-delete"),
]