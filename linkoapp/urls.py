from django.urls import path
from . import views


# urlpatterns for function based views
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('posts/',views.post_list, name='post_list'),
    path('comments/', views.comment_list, name='comment_list'),

    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('comments/<int:pk>/', views.comment_detail, name='comment_detail'),
    # path('profile/', views.profile_view, name='profile_view'),

    path('posts/new', views.post_create, name='post_create'),
    path('comments/new', views.comment_create, name='comment_create'),

    path('posts/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('comments/<int:pk>/edit', views.comment_edit, name='comment_edit'),
    
    path('posts/<int:pk>/delete', views.post_delete, name='post_delete'),
    path('comments/<int:pk>/delete', views.comment_delete, name='comment_delete'),

]

# urlpatterns for class based views
# urlpatterns = [

#     path('posts/<int:pk>/', views.post_detail, name='post_detail'),
#     path('comments/<int:pk>/', views.comment_detail, name='comment_detail'),

# # class based urlpatterns below
#     path('',views.PostList.as_view(), name='post_list'),
#     path('comments/', views.CommentList.as_view(), name='comment_list'),

#     path('posts/new', views.PostCreate.as_view(), name='post_create'),
#     path('comments/new', views.CommentCreate.as_view(), name='comment_create'),

#     path('posts/<int:pk>/edit', views.PostEdit.as_view(), name='post_edit'),
#     path('comments/<int:pk>/edit', views.CommentEdit.as_view(), name='comment_edit'),
    
#     path('posts/<int:pk>/delete', views.PostDelete.as_view(), name='post_delete'),
#     path('comments/<int:pk>/delete', views.CommentDelete.as_view(), name='comment_delete'),

# ]