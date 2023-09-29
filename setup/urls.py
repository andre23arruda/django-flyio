from rest_framework import permissions, routers
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from ping import views as ping_views
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="SSAPI",
        default_version="v1",
    ),
    public=False,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()

urlpatterns = [
    url('doc-swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url('doc-redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url('ping', ping_views.Ping.as_view(), name='ping'),
    path("admin/", admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
