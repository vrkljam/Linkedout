from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    path('',views.PostList.as_view(), name='post_list'),
    path('profile/',views.PortraitList.as_view(), name='portriat_page'),
    path('comments/', views.CommentList.as_view(), name='comment_list'),
    path('buckets/', views.BucketLists.as_view(), name='bucket_list'),

    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name='comment_detail'),
    path('portraits/<int:pk>/', views.PortraitDetail.as_view(), name='portrait_detail'),
    path('buckets/<int:pk>/', views.BuckListDetail.as_view(), name='bucket_detail'),
    
    path('posts/new', login_required(views.PostCreate.as_view()), name='post_form'),
    # path('posts/new', views.post_create, name='post_create'),
    path('comments/new', login_required(views.CommentCreate.as_view()), name='comment_form'),
    path('portraits/new', login_required(views.PortraitCreate.as_view()), name='portrait_form'),
    path('buckets/new', login_required(views.BucketListCreate.as_view()), name='bucket_form'),

    path('posts/<int:pk>/edit', login_required(views.PostEdit.as_view()), name='post_edit'),
    path('comments/<int:pk>/edit', login_required(views.CommentEdit.as_view()), name='comment_edit'),
    path('portraits/<int:pk>/edit', login_required(views.PortraitEdit.as_view()), name='portrait_edit'),
    path('buckets/<int:pk>/edit', login_required(views.BucketListEdit.as_view()), name='bucket_edit'),
        
    path('posts/<int:pk>/delete', login_required(views.PostDelete.as_view()), name='post_delete'),
    path('comments/<int:pk>/delete', login_required(views.CommentDelete.as_view()),name='comment_delete'),
    path('portraits/<int:pk>/delete', login_required(views.PortraitDelete.as_view()),name='portrait_delete'),
    path('buckets/<int:pk>/delete', login_required(views.BucketDelete.as_view()),name='bucket_delete'),

]



# class UserProfile(models.Model):
#     user=models.OneToOneField(User, on_delete=models.CASCADE)
#     location=models.CharField(max_length=100)

#     def __str__(self):
#         return self.user.username

# class Profile(models.Model):

#     is_retired=models.BooleanField(default=True)
#     previous_companies=models.TextField()
#     location=models.CharField(max_length=100)
#     photo_url=models.TextField()


#     def __str__(self):
#         return str(self.location)
    # class Meta:
    #     ordering =['location']