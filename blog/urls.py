from django.urls import path
from .views import blog_view, article_detail_view, article_create_view

app_name = 'blog'
urlpatterns= [
    path('', blog_view, name= 'blog'),
    path('articles/<int:article_id>/', article_detail_view, name = 'article_detail'),
    path('articles/create/', article_create_view, name = 'create_article'),
]