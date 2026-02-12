from django.contrib import admin
from django.urls import path, include
from rango import views

urlpatterns = [
    path('', views.index, name='index'),          
    path('about/', views.about, name='about'),    

    path('rango/', include('rango.urls')),        
    path('admin/', admin.site.urls),
]



