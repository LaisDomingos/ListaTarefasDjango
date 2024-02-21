from django.contrib import admin
from django.urls import path

from todos.views import TodoListView, TodoCrateView, TodoUpdateView, TodoDeleteView  
urlpatterns = [
    path("admin/", admin.site.urls), 
    path("", TodoListView.as_view(), name="todo_list"), 
    path("create", TodoCrateView.as_view(), name="todo_create"),
    path("update/<int:pk>", TodoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name="todo_delete"),
]
