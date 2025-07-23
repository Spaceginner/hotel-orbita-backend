from rest_framework.routers import SimpleRouter

from .views import BuildingViewSet, FloorViewSet, RoomCategoryViewSet, RoomFeatureViewSet

router = SimpleRouter()
router.register('buildings', BuildingViewSet, basename='building')
router.register('floors', FloorViewSet, basename='floor')
router.register('roomcategories', RoomCategoryViewSet)
router.register('roomfeatures', RoomFeatureViewSet)

app_name = "hotel_infrastructure"
urlpatterns = router.urls
