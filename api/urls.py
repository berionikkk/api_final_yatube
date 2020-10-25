from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )

from .views import *


router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register(r'posts/(?P<post_id>[0-9]+)/comments', CommentViewSet, basename='comments')
router.register(r'follow', FollowViewSet, basename='follows')
router.register('group', GroupViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
