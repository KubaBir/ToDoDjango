from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('add_task/', views.CreateObj.as_view(), name='add_task'),
    path('tasks/', views.ViewTasks.as_view(), name='tasks'),
    path('delete_task/<int:pk>', views.DeleteTask.as_view(), name='delete_task'),
    path('task/<int:pk>', views.TaskDetail.as_view(), name='task_detail'),
    path('update_task/<int:pk>', views.UpdateTask.as_view(), name='update_task'),
]
