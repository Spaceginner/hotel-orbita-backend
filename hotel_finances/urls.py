from rest_framework.routers import SimpleRouter

from .views import PriceViewSet


router = SimpleRouter()
router.register('prices', PriceViewSet)


app_name = 'hotel_finances'
urlpatterns = router.urls
