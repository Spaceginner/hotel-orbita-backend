from rest_framework.routers import SimpleRouter

from .views import BuildingViewSet, FloorViewSet

router = SimpleRouter()
router.register('buildings', BuildingViewSet, basename='building')
router.register('floors', FloorViewSet, basename='floor')

app_name = "hotel_infrastructure"
urlpatterns = router.urls
