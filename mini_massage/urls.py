from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from massages.views import home  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), 
    path('produits/', include('produits.urls')),  
    path('massages/', include('massages.urls')), 
    path('accounts/', include('django.contrib.auth.urls')),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
