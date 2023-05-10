from django.urls import include, path

from djoser.views import TokenDestroyView

from rest_framework import routers

from rest_framework_simplejwt.views import TokenObtainPairView

from .views import UserViewSet

app_name = 'users'

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),
    path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list-create'),
    path('auth/token/login/', TokenObtainPairView.as_view(), name='auth/token/login/'),
    path('auth/token/logout/', TokenDestroyView.as_view(), name='auth/token/logout/'),
]
