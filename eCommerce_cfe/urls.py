from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from contact_us.views import contact_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('users.urls')),
    path('products/', include('products.urls')),
    path('search/', include('search.urls')),
    path('cart/', include('carts.urls')),
    path('contact/', contact_page, name='contact-us'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)