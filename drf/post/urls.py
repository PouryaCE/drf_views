from django.urls import path
from .views import PostListView, IndexView

app_name = "post"


urlpatterns = [
    path('list/', PostListView.as_view(), name="list"),
    path('', IndexView.as_view(), name="index")
]