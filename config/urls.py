from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('medicamentos.urls')),
    path('api/', include('horarios.urls')),
    path('api/', include('confirmacoes.urls')),
    path('api/', include('receitas.urls')),

    path('api/usuarios/', include('usuarios.urls')),
    path('api/pacientes/', include('pacientes.urls')),
    path('api/cuidadores/', include('cuidadores.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )