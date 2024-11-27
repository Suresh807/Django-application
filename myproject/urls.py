# myproject/urls.py

from django.contrib import admin
from django.urls import path, include  # Import 'include' to include app URLs

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('', include('accounts.urls')),  # Include the 'accounts' app's URLs
]
