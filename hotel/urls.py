from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

app_name = 'hotel'
urlpatterns = [
    path('', include('hotel_staff.urls')),
    path('auth/', include('hotel_auth.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger/', SpectacularSwaggerView.as_view(url='/api/schema'), name='swagger-ui'),
]
