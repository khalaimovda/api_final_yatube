from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register(prefix='posts', viewset=PostViewSet, basename=None)
router.register(
    prefix=r'posts/(?P<post_id>\d+)/comments',
    viewset=CommentViewSet,
    basename='comments'
)
router.register(prefix='groups', viewset=GroupViewSet, basename=None)
router.register(prefix='follow', viewset=FollowViewSet, basename='follow')

urlpatterns = router.urls

urlpatterns += [
    path('', include('djoser.urls.jwt')),
]
