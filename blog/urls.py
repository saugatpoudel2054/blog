from django.urls import path
from .views import DefaultView, ArticleDetailView

urlpatterns = [
    path('', DefaultView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='detail'),
]
