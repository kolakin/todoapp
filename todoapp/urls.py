from django.urls import path
from . import views


urlpatterns = [
    # Adding a ToDo Task
    path('addTask/', views.addTask, name='addTask'),
    
    # Marking a Todo Task as done
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    
    #Undoing a ToDo task
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),
    
    # Delting a ToDo task
    path('deletes/<int:pk>/', views.deletes, name='deletes'),

    #Editing a Todo Task
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task')
]