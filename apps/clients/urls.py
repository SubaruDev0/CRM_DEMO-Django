# apps/clients/urls.py
from django.urls import path
from . import views

app_name = 'clients'  # namespace de la app

urlpatterns = [
    # Clientes
    path('clients/', views.ClientListView.as_view(), name='client_list'),
    path('clients/<int:pk>/', views.ClientDetailView.as_view(), name='client_detail'),
    path('clients/add/', views.ClientCreateView.as_view(), name='client_add'),
    path('clients/<int:pk>/edit/', views.ClientUpdateView.as_view(), name='client_edit'),
    path('clients/<int:pk>/delete/', views.ClientDeleteView.as_view(), name='client_delete'),

    # Reportes
    path('reports/', views.ReportListView.as_view(), name='report_list'),
    path('reports/<int:pk>/', views.ReportDetailView.as_view(), name='report_detail'),
    path('reports/add/', views.ReportCreateView.as_view(), name='report_add'),
    path('reports/<int:pk>/edit/', views.ReportUpdateView.as_view(), name='report_edit'),
    path('reports/<int:pk>/delete/', views.ReportDeleteView.as_view(), name='report_delete'),
]
