from django.contrib import admin
from django.urls import path
from .views import Homepage, CreateAccountView, Dashboard, AddItem, EditItem, DeleteItem
from django.contrib.auth import views as auth_views
urlpatterns = [
path('', Homepage.as_view(), name='index'),
path('dashboard/', Dashboard.as_view(), name='dashboard'),
path('add-stock/', AddItem.as_view(), name="addstock"),
path('edit-stock/<int:pk>', EditItem.as_view(), name="editstock"),
path('delete-item/<int:pk>', DeleteItem.as_view(), name='delete-item'),
path('createaccount/', CreateAccountView.as_view(), name='createaccount'),
path('login/', auth_views.LoginView.as_view(template_name = 'inventory/login.html'), name='login'),
path('logout/', auth_views.LogoutView.as_view(template_name = 'inventory/logout.html'), name='logout'),
]
