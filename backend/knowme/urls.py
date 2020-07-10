from django.urls import path
from . import views


app_name = 'knowme'

urlpatterns = [
    path("register", views.registration_view, name='register'),
    path('login', views.login_view, name='login'),
    path('projects', views.user_projects_list, name='projects'),
    path('add-project', views.add_projects_to_account, name='add-project'),
    path('delete-project/<int:pk>/', views.delete_project, name='delete-project'),
    path('portfolio/<uuid:pk>/', views.portfolio, name='portfolio'),
    path('update-account', views.update_account_details, name='update-account'),
    path('update-password', views.update_account_password, name='update-password'),
    path('templates', views.choose_template, name='templates')
]
