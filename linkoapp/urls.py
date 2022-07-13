from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


# urlpatterns for function based views
urlpatterns = [
    path('', views.Home.as_view(), name="home"),

    path('posts/',views.PostList.as_view(), name='post_list'),
    path('comments/', views.CommentList.as_view(), name='comment_list'),

    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name='comment_detail'),
    # path('profile/', views.profile_view, name='profile_view'),

    path('posts/new', login_required(views.PostCreate.as_view()), name='post_form'),
    path('comments/new', login_required(views.CommentCreate.as_view()), name='comment_form'),

    path('posts/<int:pk>/edit', login_required(views.PostEdit.as_view()), name='post_edit'),
    path('comments/<int:pk>/edit', login_required(views.CommentEdit.as_view()), name='comment_edit'),
    # path('posts/<int:pk>/redit', views.post_redit, name='post_redit'),
    
    path('posts/<int:pk>/delete', login_required(views.PostDelete.as_view()), name='post_delete'),
    path('comments/<int:pk>/delete', views.comment_delete, name='comment_delete'),

]

# urlpatterns for class based views
# urlpatterns = [

#     path('posts/<int:pk>/', views.post_detail, name='post_detail'),
#     path('comments/<int:pk>/', views.comment_detail, name='comment_detail'),

# # class based urlpatterns below
#     path('posts/',views.PostList.as_view(), name='post_list'),
#     path('comments/', views.CommentList.as_view(), name='comment_list'),

#     path('posts/new', views.PostCreate.as_view(), name='post_create'),
#     path('comments/new', views.CommentCreate.as_view(), name='comment_create'),

#     path('posts/<int:pk>/edit', views.PostEdit.as_view(), name='post_edit'),
#     path('comments/<int:pk>/edit', views.CommentEdit.as_view(), name='comment_edit'),
    
#     path('posts/<int:pk>/delete', views.PostDelete.as_view(), name='post_delete'),
#     path('comments/<int:pk>/delete', views.CommentDelete.as_view(), name='comment_delete'),

# ]