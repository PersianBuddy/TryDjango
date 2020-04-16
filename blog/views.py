from django.shortcuts import render , get_object_or_404 , redirect
from .models import Article
from .forms import  CreateArticleForm

# Create your views here.
def blog_view(request, *args, **kwargs):
    articles_list = Article.objects.all()
    context = {
        'articles_list': articles_list
    }
    return render(request,'blog.html', context)


def article_detail_view(request, article_id, *args, **kwargs):
    article_obj = get_object_or_404(Article, id = article_id)
    if request.method == 'POST':
        article_obj.delete()
        return redirect('/blog/')
    context = {
        'article' : article_obj,
    }
    return render(request,'articles/article_detail.html', context)

def article_create_view(request, *args, **kwargs):
    form = CreateArticleForm()
    if request.method == 'POST':
        form = CreateArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/blog/')

    context = {
        'form' : form
    }
    return render(request, 'articles/create_article.html', context)