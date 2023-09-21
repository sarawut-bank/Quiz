from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('success', views.success, name='success'),
    path('alldata', views.allData, name='allData'),
    path('delete_data', views.delete_data, name='delete_data'),
    path('approve_status/<int:data_id>/', views.approve_status, name='approve_status'),
    path('reject_status/<int:data_id>/', views.reject_status, name='reject_status'),
]
