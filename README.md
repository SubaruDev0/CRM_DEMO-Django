# CRM Demo - Django

## Descripción

Este es un sistema CRM (Customer Relationship Management) desarrollado en Django que permite gestionar clientes, reportes y archivos asociados. [1](#0-0) 

## Características

- **Gestión de Clientes**: Crear, leer, actualizar y eliminar clientes [2](#0-1) 
- **Gestión de Reportes**: Administrar reportes asociados a clientes [3](#0-2) 
- **Subida de Archivos**: Adjuntar archivos a los reportes [4](#0-3) 
- **Panel de Administración**: Interface administrativa completa [5](#0-4) 
- **Búsqueda y Filtrado**: Funcionalidad de búsqueda para clientes y reportes [6](#0-5) 

## Requisitos del Sistema

- Python 3.8+
- Django 4.0+
- SQLite (incluido con Python)

## Instalación y Configuración

### 1. Crear el Entorno Virtual

```bash
# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
# En Windows:
.venv\Scripts\activate
# En macOS/Linux:
source .venv/bin/activate
```

### 2. Instalar Dependencias

```bash
# Instalar Django
pip install django

# Si tienes un archivo requirements.txt (crear uno con):
pip freeze > requirements.txt
```

### 3. Configuración del Proyecto

El proyecto utiliza la siguiente configuración: [7](#0-6) 

La configuración de base de datos utiliza SQLite: [8](#0-7) 

### 4. Crear y Aplicar Migraciones

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate
```

### 5. Crear Superusuario

```bash
python manage.py createsuperuser
```

### 6. Ejecutar el Servidor de Desarrollo

```bash
python manage.py runserver
```

El servidor estará disponible en `http://127.0.0.1:8000/` [9](#0-8) 

## Estructura del Proyecto

```
CRM_DEMO-Django/
├── manage.py
├── crm_web/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apps/
│   └── clients/
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       ├── admin.py
│       ├── apps.py
│       ├── tests.py
│       └── migrations/
└── templates/
    ├── base.html
    ├── clients/
    └── reports/
```

## Modelos de Datos

### Cliente (Client)
- `name`: Nombre completo del cliente
- `email`: Email único por cliente  
- `phone`: Teléfono opcional [2](#0-1) 

### Reporte (Report)
- `client`: Relación con Cliente
- `title`: Título del reporte
- `description`: Descripción opcional
- `created_at`: Fecha de creación [3](#0-2) 

### Archivo de Reporte (ReportFile)
- `report`: Relación con Reporte
- `file`: Archivo subido
- `uploaded_at`: Fecha de subida [4](#0-3) 

## URLs Principales

### Clientes
- `/clients/` - Lista de clientes
- `/clients/add/` - Crear cliente
- `/clients/<id>/` - Detalle de cliente
- `/clients/<id>/edit/` - Editar cliente
- `/clients/<id>/delete/` - Eliminar cliente

### Reportes
- `/reports/` - Lista de reportes
- `/reports/add/` - Crear reporte
- `/reports/<id>/` - Detalle de reporte
- `/reports/<id>/edit/` - Editar reporte
- `/reports/<id>/delete/` - Eliminar reporte [10](#0-9) 

## Panel de Administración

El panel de administración está disponible en `/admin/` y incluye:

- Gestión completa de clientes con búsqueda [11](#0-10) 
- Gestión de reportes con archivos inline [5](#0-4) 
- Subida de archivos directamente desde el reporte [12](#0-11) 

## Funcionalidades Adicionales

### Búsqueda
- **Clientes**: Búsqueda por nombre [13](#0-12) 
- **Reportes**: Búsqueda por título de reporte o nombre de cliente [14](#0-13) 

### Paginación
Tanto clientes como reportes incluyen paginación de 10 elementos por página [15](#0-14) 

### Configuración Regional
El proyecto está configurado para español chileno: [16](#0-15) 

## Archivos Media

Los archivos subidos se guardan en la carpeta `media/report_files/` [17](#0-16) 

La configuración de archivos media está en: [18](#0-17) 

## Desarrollo

### Comandos Útiles

```bash
# Ejecutar el servidor de desarrollo
python manage.py runserver

# Crear migraciones después de cambios en modelos
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Acceder al shell de Django
python manage.py shell

# Crear superusuario para admin
python manage.py createsuperuser

# Recopilar archivos estáticos (para producción)
python manage.py collectstatic
```

### Estructura de Vistas

El proyecto utiliza vistas basadas en clases (CBV) para operaciones CRUD: [19](#0-18) 

## Notas

- Este es un proyecto de demostración con configuración de desarrollo
- La clave secreta está hardcodeada y debe cambiarse en producción [20](#0-19) 
- Se utiliza SQLite para simplicidad, considerar PostgreSQL para producción
- Los archivos media se sirven en desarrollo automáticamente [21](#0-20)

### Citations

**File:** crm_web/settings.py (L11-13)
```python
SECRET_KEY = 'django-insecure-9yz5=bnr-i@b=i(a+h*@wer5evbp3-*l*&cpgmufks=h8^0416'
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
```

**File:** crm_web/settings.py (L26-28)
```python
    # apps del proyecto
    'apps.clients.apps.ClientsConfig',
]
```

**File:** crm_web/settings.py (L75-80)
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',   # base simple para práctica
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

**File:** crm_web/settings.py (L95-99)
```python
LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_L10N = True
USE_TZ = True
```

**File:** crm_web/settings.py (L108-109)
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

**File:** apps/clients/models.py (L7-14)
```python
class Client(models.Model):
    name = models.CharField(max_length=100)  # Nombre completo del cliente
    email = models.EmailField(unique=True)   # Email único por cliente
    phone = models.CharField(max_length=20, blank=True)  # Teléfono opcional

    def __str__(self):
        # Esto se muestra en admin y relaciones
        return self.name
```

**File:** apps/clients/models.py (L20-32)
```python
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
```

**File:** apps/clients/models.py (L38-48)
```python
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
```

**File:** apps/clients/admin.py (L7-9)
```python
class ReportFileInline(admin.TabularInline):
    model = ReportFile
    extra = 1  # Cuántas filas extra para subir archivos
```

**File:** apps/clients/admin.py (L14-16)
```python
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'created_at')  # Columnas en la lista de reportes
    inlines = [ReportFileInline]  # Archivos relacionados se muestran inline
```

**File:** apps/clients/admin.py (L21-23)
```python
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')  # Columnas en la lista de clientes
    search_fields = ('name', 'email')  # Permite buscar clientes por nombre o email
```

**File:** apps/clients/views.py (L3-3)
```python
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
```

**File:** apps/clients/views.py (L16-16)
```python
    paginate_by = 10  # 10 clientes por página
```

**File:** apps/clients/views.py (L18-27)
```python
    def get_queryset(self):
        """Filtra clientes según parámetro de búsqueda 'q'"""
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        
        if query:
            # Filtrar clientes cuyo nombre contenga el texto de búsqueda
            qs = qs.filter(name__icontains=query)
        
        return qs
```

**File:** apps/clients/views.py (L84-89)
```python
        if query:
            # CORREGIDO: Buscar en título del reporte Y en nombre del cliente relacionado
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(client__name__icontains=query)  # Acceder al nombre del cliente via relación
            )
```

**File:** apps/clients/urls.py (L7-21)
```python
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
```

**File:** crm_web/urls.py (L12-14)
```python
# Para servir archivos media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
