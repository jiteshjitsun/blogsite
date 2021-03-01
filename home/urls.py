from django.urls import path
from . import views
from .views import AddCategoryView, AddPostView, DeletePostView, HomeView, PostView, UpdatePostView, CategoryView, AddCategoryView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog/<int:pk>', PostView.as_view(), name='details'),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('blog/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('blog/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', views.CategoryView, name="category"),
    # path('likes/<int:pk>', views.LikeView, name='like_post'),
]
