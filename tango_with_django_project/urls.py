from django.contrib import admin
from django.urls import path, include
from rango import views as rango_views

urlpatterns = [
    path('', rango_views.index, name='index'),

    # Support ABOUT at project level too (so /about and /about/ work)
    path('about', rango_views.about, name='about'),
    path('about/', rango_views.about, name='about'),

    # Rango app URLs (so /rango/... works)
    path('rango/', include('rango.urls')),

    path('admin/', admin.site.urls),
]





