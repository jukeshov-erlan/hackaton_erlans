from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import CommentView, RatingView, LikeView, BookMarkView

router = SimpleRouter()
router.register('comments', CommentView)
router.register('ratings', RatingView)
router.register('likes', LikeView)
router.register('bookmarks', BookMarkView)



urlpatterns = [
    path('', include(router.urls))
]