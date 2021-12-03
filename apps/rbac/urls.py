from . import views
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register('user', views.UserViewSet)
router.register('group', views.GroupViewSet)
router.register('premission', views.PermissionViewSet)
urlpatterns = router.urls