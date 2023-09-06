from django.urls import path
from .views import PostList, PostDetail, UserList, UserDetail  # new
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("users/", UserList.as_view()),  # new
    path("users/<int:pk>/", UserDetail.as_view()),  # new
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("", PostList.as_view(), name="post_list"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
# # The code below perfom urls like the above but it uses viewsets to make it simple
# from rest_framework.routers import SimpleRouter
# from .views import UserViewSet, PostViewSet

# router = SimpleRouter()
# router.register("users", UserViewSet, basename="users")
# router.register("", PostViewSet, basename="posts")
# urlpatterns = router.urls
