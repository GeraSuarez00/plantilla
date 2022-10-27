from rest_framework import routers
from .views import PersonViewSet
from .views import AttendantViewSet
from .views import StudentViewSet
from .views import Student_AttendantViewSet

router= routers.SimpleRouter()
router.register('Person',PersonViewSet)
router.register('Attendant',AttendantViewSet)
router.register('Student',StudentViewSet)
router.register('Student_Attendant',Student_AttendantViewSet)
urlpatterns = router.urls
