from django.urls import path

from blog_app.views import PostDetailView, PostListView

urlpatterns = [
    path(
        '<year>/<month>/<day>/<slug>',
        PostDetailView.as_view(),
        name='post_detail'
    ),
    path('', PostListView.as_view(), name='post_list'),
]