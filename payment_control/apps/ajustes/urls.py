from rest_framework import routers
from .views import DatosMaestrosViewSet

router= routers.SimpleRouter()
router.register('DatosMaestros',DatosMaestrosViewSet)

urlpatterns = router.urls