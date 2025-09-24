from django.contrib import admin
from .models import Client, Report, ReportFile

# ------------------------------------------------------------
# Permite subir archivos directamente desde el reporte en el admin
# ------------------------------------------------------------
class ReportFileInline(admin.TabularInline):
    model = ReportFile
    extra = 1  # Cuántas filas extra para subir archivos

# ------------------------------------------------------------
# Configuración del admin para Report
# ------------------------------------------------------------
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'created_at')  # Columnas en la lista de reportes
    inlines = [ReportFileInline]  # Archivos relacionados se muestran inline

# ------------------------------------------------------------
# Configuración del admin para Client
# ------------------------------------------------------------
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')  # Columnas en la lista de clientes
    search_fields = ('name', 'email')  # Permite buscar clientes por nombre o email

# ------------------------------------------------------------
# Registrar modelos en el admin
# ------------------------------------------------------------
admin.site.register(Client, ClientAdmin)
admin.site.register(Report, ReportAdmin)
