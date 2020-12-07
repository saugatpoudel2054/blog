from django.urls import path
from .views import DefaultView, ArticleDetailView, AddNewArticle, UpdatePost, DeletePost

urlpatterns = [
    path('', DefaultView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='detail'),
    path('new/', AddNewArticle.as_view(), name='post_new'),
    path('article/<int:pk>/edit/', UpdatePost.as_view(), name='post_edit'),
    path('article/<int:pk>/delete/', DeletePost.as_view(), name='post_delete'),
]
