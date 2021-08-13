from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('index/', include('index.urls')),
    path('', RedirectView.as_view(url='index/', permanent=True)),    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
