from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.laboratorio_list, name='laboratorio_list'), 
    path('create/', views.laboratorio_create, name='laboratorio_create'), 
    path('<int:pk>/edit/', views.laboratorio_update, name='laboratorio_update'),    
    path('<int:pk>/delete/', views.laboratorio_delete, name='laboratorio_delete'),
    path('<int:pk>/', views.laboratorio_detail, name='laboratorio_detail'), # Detalle del laboratorio
]

