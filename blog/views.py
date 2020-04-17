from django.shortcuts import reverse
from .models import Article
from .forms import  CreateArticleForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)

# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'blog.html'
    context_object_name = 'articles_list'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'


class ArticleCreateView(CreateView):
    form_class = CreateArticleForm
    template_name = 'articles/create_article.html'


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = CreateArticleForm
    template_name = 'articles/update_article.html'


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'articles/delete_article.html'
    def get_success_url(self):
        return reverse('blog:blog')

# def blog_view(request, *args, **kwargs):
#     articles_list = Article.objects.all()
#     context = {
#         'articles_list': articles_list
#     }
#     return render(request,'blog.html', context)
#
#
# def article_detail_view(request, article_id, *args, **kwargs):
#     article_obj = get_object_or_404(Article, id = article_id)
#     if request.method == 'POST':
#         article_obj.delete()
#         return redirect('/blog/')
#     context = {
#         'article' : article_obj,
#     }
#     return render(request,'articles/article_detail.html', context)
#
# def article_create_view(request, *args, **kwargs):
#     form = CreateArticleForm()
#     if request.method == 'POST':
#         form = CreateArticleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/blog/')
#
#     context = {
#         'form' : form
#     }
#     return render(request, 'articles/create_article.html', context)