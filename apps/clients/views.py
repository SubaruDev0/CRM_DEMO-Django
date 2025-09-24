from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Client, Report

# ---------- VISTAS PARA CLIENTES ----------

class ClientListView(ListView):
    """
    Vista para listar todos los clientes con paginación y búsqueda
    """
    model = Client
    template_name = 'clients/client_list.html'
    context_object_name = 'clients'  # Nombre del objeto en el template
    paginate_by = 10  # 10 clientes por página

    def get_queryset(self):
        """Filtra clientes según parámetro de búsqueda 'q'"""
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        
        if query:
            # Filtrar clientes cuyo nombre contenga el texto de búsqueda
            qs = qs.filter(name__icontains=query)
        
        return qs


class ClientDetailView(DetailView):
    """
    Vista para mostrar los detalles de un cliente específico
    """
    model = Client
    template_name = 'clients/client_detail.html'
    context_object_name = 'client'


class ClientCreateView(CreateView):
    """
    Vista para crear un nuevo cliente
    """
    model = Client
    fields = ['name', 'email']  # Campos que se mostrarán en el formulario
    template_name = 'clients/client_form.html'
    success_url = reverse_lazy('clients:client_list')  # Redirigir después de crear


class ClientUpdateView(UpdateView):
    """
    Vista para actualizar un cliente existente
    """
    model = Client
    fields = ['name', 'email']
    template_name = 'clients/client_form.html'
    success_url = reverse_lazy('clients:client_list')  # Redirigir después de actualizar


class ClientDeleteView(DeleteView):
    """
    Vista para eliminar un cliente (con confirmación)
    """
    model = Client
    template_name = 'clients/client_confirm_delete.html'
    success_url = reverse_lazy('clients:client_list')  # Redirigir después de eliminar


# ---------- VISTAS PARA REPORTES ----------

class ReportListView(ListView):
    """
    Vista para listar todos los reportes con paginación y búsqueda
    """
    model = Report
    template_name = 'reports/report_list.html'  # Template CORREGIDO
    context_object_name = 'reports'
    paginate_by = 10

    def get_queryset(self):
        """Filtra reportes según parámetro de búsqueda 'q'"""
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        
        if query:
            # CORREGIDO: Buscar en título del reporte Y en nombre del cliente relacionado
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(client__name__icontains=query)  # Acceder al nombre del cliente via relación
            )
        
        return qs


class ReportDetailView(DetailView):
    """
    Vista para mostrar los detalles de un reporte específico
    """
    model = Report
    template_name = 'reports/report_detail.html'  # CORREGIDO
    context_object_name = 'report'


# ---------- VISTAS PARA REPORTES ----------

class ReportCreateView(CreateView):
    model = Report
    fields = ['title', 'client', 'created_at']
    template_name = 'reports/report_form.html'
    success_url = reverse_lazy('clients:report_list')  # CAMBIAR: 'reports:' por 'clients:'

class ReportUpdateView(UpdateView):
    model = Report
    fields = ['title', 'client', 'created_at']
    template_name = 'reports/report_form.html'
    success_url = reverse_lazy('clients:report_list')  # CAMBIAR: 'reports:' por 'clients:'

class ReportDeleteView(DeleteView):
    model = Report
    template_name = 'reports/report_confirm_delete.html'
    success_url = reverse_lazy('clients:report_list')  # CAMBIAR: 'reports:' por 'clients:'