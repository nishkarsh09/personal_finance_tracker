from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
urlpatterns = [
    path('', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('add-income/', views.add_income, name='add_income'), 
    path('edit-income/<int:pk>/', views.edit_income, name='edit_income'),  
    path('delete-income/<int:pk>/', views.delete_income, name='delete_income'),  
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]