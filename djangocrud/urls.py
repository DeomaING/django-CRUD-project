
from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('tasks/', views.tasks, name="tasks"),
    path('tasks/completed/', views.task_completed, name="task_completed"),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name="signin"),
    path('tasks/create/', views.createNewTask, name='createNewTask'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('tasks/<int:task_id>/complete', views.completeTask, name='completeTask'),
    path('tasks/<int:task_id>/delete', views.deleteTask, name='deleteTask'),

]
