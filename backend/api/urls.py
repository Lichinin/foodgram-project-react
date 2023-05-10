from django.urls import include, path

from rest_framework import routers

from .views import UserViewSet

app_name = 'users'

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list-create'),
]
