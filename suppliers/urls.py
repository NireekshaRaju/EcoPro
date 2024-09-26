from django.urls import path
from . import views

urlpatterns = [
    # path('addproducts/', views.addproducts, name='addproducts'),
    # path('sell/', views.sell, name='sell'),
    path('selldashboard/', views.selldashboard, name='selldashboard'),
    path('tables/', views.tables, name='tables'),
    path('billing/', views.billing, name='billing'),
    path('notifications/', views.notifications, name='notifications'),
    path('profile/', views.profile, name='profile'),
    path('create_staff/', views.CreateStaff.as_view(), name='create_staff'),
    path('delete_user/', views.delete_user.as_view(), name='delete_user'),
    path('delete_uses/', views.delete_uses.as_view(), name='delete_uses'),
    path('update_staff/', views.update_staff.as_view(), name='update_staff'),
]