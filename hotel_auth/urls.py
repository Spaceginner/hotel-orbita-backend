from django.urls import path

from .views import SignInApiView, SignOutApiView

app_name = 'hotel_auth'
urlpatterns = [
    path('sign-in/', SignInApiView.as_view(), name='signin-api'),
    path('sign-out/', SignOutApiView.as_view(), name='singout-api'),
    # path('sign-up', SignUpApiView.as_view(), name='signup-api'),
]
