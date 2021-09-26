from django.urls import include, path
from rest_framework import routers
from api.views import TagViewset, UserViewset, PostViewset

router = routers.DefaultRouter()
router.register(r'users', UserViewset)
router.register(r'posts', PostViewset)
router.register(r'tags', TagViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework')),
]