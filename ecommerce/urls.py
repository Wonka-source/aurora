from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("home.urls")),
    path("shop/", include("shop.urls")),
    path("cart/", include("cart.urls")),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('watch_repair/', include('watch_repair.urls')),
    path('blog/', include('blog.urls')),
    path('staff/', include('staff.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = "ecommerce.views.handler404"
handler500 = "ecommerce.views.handler500"
handler403 = "ecommerce.views.handler403"
handler405 = "ecommerce.views.handler405"
