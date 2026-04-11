from django.contrib import admin
from django.urls import path, include

# Ye dono imports add karna bohot zaroori hai
from django.conf import settings             
from django.conf.urls.static import static   
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
]

# Ye line Django ko batati hai ki images browser ko kaise bhejni hain
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)