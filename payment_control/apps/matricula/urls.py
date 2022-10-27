from rest_framework import routers
from .views import RegistrationViewSet
from .views import PaymentViewSet

router= routers.SimpleRouter()
router.register('Registration',RegistrationViewSet)
router.register('Payment',PaymentViewSet)
urlpatterns = router.urls

