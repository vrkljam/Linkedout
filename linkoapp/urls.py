from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.Home.as_view(), name="home"),

    path('posts/',views.PostList.as_view(), name='post_list'),
    path('profile/',views.ProfileList.as_view(), name='profile_page'),

    path('comments/', views.CommentList.as_view(), name='comment_list'),

    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name='comment_detail'),
    
    path('posts/new', login_required(views.PostCreate.as_view()), name='post_form'),
    path('comments/new', login_required(views.CommentCreate.as_view()), name='comment_form'),

    path('posts/<int:pk>/edit', login_required(views.PostEdit.as_view()), name='post_edit'),
    path('comments/<int:pk>/edit', login_required(views.CommentEdit.as_view()), name='comment_edit'),
    # path('posts/<int:pk>/redit', views.post_redit, name='post_redit'),
    
    path('posts/<int:pk>/delete', login_required(views.PostDelete.as_view()), name='post_delete'),
    path('comments/<int:pk>/delete', login_required(views.CommentDelete.as_view()),name='comment_delete'),

]