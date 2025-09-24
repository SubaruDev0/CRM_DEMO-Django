from django.db import models
from django.utils import timezone

# ------------------------------------------------------------
# Cliente de la consultora
# ------------------------------------------------------------
class Client(models.Model):
    name = models.CharField(max_length=100)  # Nombre completo del cliente
    email = models.EmailField(unique=True)   # Email único por cliente
    phone = models.CharField(max_length=20, blank=True)  # Teléfono opcional

    def __str__(self):
        # Esto se muestra en admin y relaciones
        return self.name


# ------------------------------------------------------------
# Reporte asociado a un cliente
# ------------------------------------------------------------
class Report(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='reports'
    )  # Cada report pertenece a un cliente. Si se borra el cliente, se borran sus reportes
    title = models.CharField(max_length=150)  # Título del reporte
    description = models.TextField(blank=True)  # Descripción opcional
    created_at = models.DateTimeField(default=timezone.now)  # Fecha de creación

    def __str__(self):
        # Nombre del reporte junto al cliente
        return f"{self.title} - {self.client.name}"


# ------------------------------------------------------------
# Archivos asociados a un reporte
# ------------------------------------------------------------
class ReportFile(models.Model):
    report = models.ForeignKey(
        Report,
        on_delete=models.CASCADE,
        related_name='files'
    )  # Cada archivo pertenece a un reporte. Si se borra el reporte, se borran sus archivos
    file = models.FileField(upload_to='report_files/')  # Carpeta dentro de MEDIA_ROOT
    uploaded_at = models.DateTimeField(default=timezone.now)  # Fecha de subida del archivo

    def __str__(self):
        return f"{self.file.name} ({self.report.title})"
