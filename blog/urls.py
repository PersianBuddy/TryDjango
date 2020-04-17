from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = 'blog'
urlpatterns= [
    path('', ArticleListView.as_view(), name= 'blog'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name = 'article_detail'),
    path('articles/create/', ArticleCreateView.as_view(), name = 'create_article'),
    path('articles/<int:pk>/update/', ArticleUpdateView.as_view(), name = 'update_article'),
    path('articles/<int:pk>/delete/', ArticleDeleteView.as_view(), name = 'delete_article'),
]