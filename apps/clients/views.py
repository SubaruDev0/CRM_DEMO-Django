# apps/clients/views.py 
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q, Count
from .models import Client, Report

# ---------- DASHBOARD ----------
def dashboard_view(request):
    """Dashboard principal con métricas"""
    # Métricas básicas
    total_clients = Client.objects.count()
    total_reports = Report.objects.count()
    
    # Clientes con más reportes
    top_clients = Client.objects.annotate(
        report_count=Count('reports')
    ).order_by('-report_count')[:5]
    
    # Reportes recientes
    recent_reports = Report.objects.select_related('client').order_by('-created_at')[:5]
    
    context = {
        'total_clients': total_clients,
        'total_reports': total_reports,
        'top_clients': top_clients,
        'recent_reports': recent_reports,
    }
    
    return render(request, 'dashboard.html', context)

# ---------- VISTAS PARA CLIENTES ----------
class ClientListView(ListView):
    """Vista para listar todos los clientes con paginación y búsqueda"""
    model = Client
    template_name = 'clients/client_list.html'
    context_object_name = 'clients'
    paginate_by = 10

    def get_queryset(self):
        """Filtra clientes según parámetro de búsqueda 'q'"""
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        
        if query:
            qs = qs.filter(
                Q(name__icontains=query) | 
                Q(email__icontains=query)
            )
        
        return qs

class ClientDetailView(DetailView):
    """Vista para mostrar los detalles de un cliente específico"""
    model = Client
    template_name = 'clients/client_detail.html'
    context_object_name = 'client'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregar reportes del cliente al contexto
        context['reports'] = self.object.reports.all().order_by('-created_at')
        return context

class ClientCreateView(CreateView):
    """Vista para crear un nuevo cliente"""
    model = Client
    fields = ['name', 'email', 'phone']  # Incluir phone
    template_name = 'clients/client_form.html'
    success_url = reverse_lazy('clients:client_list')

class ClientUpdateView(UpdateView):
    """Vista para actualizar un cliente existente"""
    model = Client
    fields = ['name', 'email', 'phone']  # Incluir phone
    template_name = 'clients/client_form.html'
    success_url = reverse_lazy('clients:client_list')

class ClientDeleteView(DeleteView):
    """Vista para eliminar un cliente (con confirmación)"""
    model = Client
    template_name = 'clients/client_confirm_delete.html'
    success_url = reverse_lazy('clients:client_list')

# ---------- VISTAS PARA REPORTES ----------
class ReportListView(ListView):
    """Vista para listar todos los reportes con paginación y búsqueda"""
    model = Report
    template_name = 'reports/report_list.html' 
    context_object_name = 'reports'
    paginate_by = 10

    def get_queryset(self):
        """Filtra reportes según parámetro de búsqueda 'q'"""
        qs = Report.objects.select_related('client')  # Optimización
        query = self.request.GET.get('q')
        
        if query:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(client__name__icontains=query)
            )
        
        return qs.order_by('-created_at')

class ReportDetailView(DetailView):
    """Vista para mostrar los detalles de un reporte específico"""
    model = Report
    template_name = 'reports/report_detail.html'  
    context_object_name = 'report'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregar archivos del reporte
        context['files'] = self.object.files.all()
        return context

class ReportCreateView(CreateView):
    """Vista para crear un nuevo reporte"""
    model = Report
    fields = ['title', 'description', 'client']  
    template_name = 'reports/report_form.html'  
    success_url = reverse_lazy('clients:report_list')

class ReportUpdateView(UpdateView):
    """Vista para actualizar un reporte existente"""
    model = Report
    fields = ['title', 'description', 'client']
    template_name = 'reports/report_form.html'  
    success_url = reverse_lazy('clients:report_list')

class ReportDeleteView(DeleteView):
    """Vista para eliminar un reporte (con confirmación)"""
    model = Report
    template_name = 'reports/report_confirm_delete.html'  
    success_url = reverse_lazy('clients:report_list')