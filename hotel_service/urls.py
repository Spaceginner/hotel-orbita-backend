from rest_framework.routers import SimpleRouter

from .views import ServiceViewSet, MealPlanViewSet, AdditionalOptionViewSet

router = SimpleRouter()
router.register('mealplans', MealPlanViewSet)
router.register('services', ServiceViewSet)
router.register('options', AdditionalOptionViewSet)

app_name = 'hotel_service'
urlpatterns = router.urls
