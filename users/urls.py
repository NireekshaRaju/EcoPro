
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('products/', views.products, name='products'),
    path('signup/', views.signup, name='signup'),
    path('create_staff/', views.CreateStaff.as_view(), name='create_staff'),
    path('view_user/', views.ViewUser.as_view(), name='view_user'),
    path('login_check/', views.login_check.as_view(), name='login_check'),
    path('delete_user/', views.delete_user.as_view(), name='delete_user'),
    path('update_staff/', views.update_staff.as_view(), name='update_staff'),
]

