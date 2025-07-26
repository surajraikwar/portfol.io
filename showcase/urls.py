from django.urls import path
from . import views


app_name = 'showcase'

urlpatterns = [
    path("register/", views.registration_view, name='registration'),
    path('login/', views.login_view, name='login'),
    path('projects/', views.user_projects_list, name='projects'),
    path('add-project/', views.add_projects_to_account, name='add_projects'),
    path('delete-project/<int:pk>/', views.delete_project, name='delete_project'),
    path('showcase/<uuid:pk>/', views.portfolio, name='portfolio'),
    path('update-account/', views.update_account_details, name='update_account_details'),
    path('update-password/', views.update_account_password, name='update_account_password'),
    path('templates/', views.choose_template, name='choose_template')
]
