from django.urls import include, path
from rest_framework import routers
from api.views import BanksViewSet,BranchesViewSet

router = routers.DefaultRouter()
router.register(r'banks', BanksViewSet)
router.register(r'branches', BranchesViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
