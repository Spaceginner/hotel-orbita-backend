from django.urls import path, include

app_name = 'hotel'
urlpatterns = [
    path('', include('hotel_staff.urls')),
    path('auth/', include('hotel_auth.urls'))
]
