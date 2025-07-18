from rest_framework.routers import SimpleRouter

from .views import StaffViewSet, DepartmentViewSet, DesignationViewSet

router = SimpleRouter()
router.register('staff', StaffViewSet)
router.register('departments', DepartmentViewSet)
router.register('designations', DesignationViewSet)

app_name = 'hotel_staff'
urlpatterns = router.urls
