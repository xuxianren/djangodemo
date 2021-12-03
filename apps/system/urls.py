from . import views
from rest_framework import routers



router = routers.DefaultRouter(trailing_slash=False)
router.register('', views.SystemViewSet, basename='system')
urlpatterns = router.urls