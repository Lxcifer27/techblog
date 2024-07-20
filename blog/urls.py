from django.urls import path
from . import views
from .views import HomeView, ArticleView, AddBlogView, AddCategoryView, UpdateBlogView, DeleteBlogView, dashboard, CategoryView, CategoryListView, LikeView


urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleView.as_view(), name="article"),
    path('add-blog/', AddBlogView.as_view(), name="AddBlog"),
    path('add-category/', AddCategoryView.as_view(), name="AddCategory"),
    path('article/update-blog/<int:pk>', UpdateBlogView.as_view(), name="UpdateBlog"),
    path('article/<int:pk>/delete-blog', DeleteBlogView.as_view(), name="DeleteBlog"),
    path('dashboard/',views.dashboard, name="dashboard"),
    path('category/<str:cats>/', CategoryView, name="Category"),
    path('category-list/', CategoryListView, name="CategoryList"),
    path('like/<int:pk>', LikeView, name="like_post"),
]