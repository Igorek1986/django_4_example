from django.urls import path
from .views import post_comment, post_detail, post_list, PostListView, post_share

app_name = "blog"

urlpatterns = [
    # path("", post_list, name="post_list"),
    path("", PostListView.as_view(), name="post_list"),
    # path("<int:id>/", post_detail, name="post_detail"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/",
        post_detail,
        name="post_detail",
    ),
    path("<int:post_id>/share/", post_share, name="post_share"),
    path("<int:post_id>/", post_comment, name="post_comment"),
]
