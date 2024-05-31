from django.urls import path
from . import views
from .views import HomeView, ArticleView, AddBlogView, UpdateBlogView, DeleteBlogView, dashboard


urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleView.as_view(), name="article"),
    path('add-blog/', AddBlogView.as_view(), name="AddBlog"),
    path('article/update-blog/<int:pk>', UpdateBlogView.as_view(), name="UpdateBlog"),
    path('article/<int:pk>/delete-blog', DeleteBlogView.as_view(), name="DeleteBlog"),
    path('dashboard/',views.dashboard, name="dashboard")
]