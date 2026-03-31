from django.contrib import admin
from django.urls import path, include # include ko import karna zaroori hai

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')), # Ye line add karni hai
]