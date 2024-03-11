from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.landing_page_view, name='landing_page'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('campaign/', include('campaign.urls')),
    # Include other apps' URLs here
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
