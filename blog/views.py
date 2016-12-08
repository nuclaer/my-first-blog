from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.models import User

from blog.models import Article
from blog.forms import ArticleForm


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


def home(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')


def group(request):
    return render(request, 'blog/site.html')


def show_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'blog/article.html', {'article': article})


def view_about(request):
    return render('about.html', RequestContext(request))


def site(request):
    return render(request, 'blog/site.html')


class CreateArticleView(LoginRequiredMixin, CreateView):
    template_name = 'blog/create_article.html'
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('create_article')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Article "{}" successfully created.'.format(form.cleaned_data['title'].encode('utf-8'))
        )
        return HttpResponseRedirect(self.success_url)


class UserListView(ListView):
    model = User
    template_name = 'blog/users.html'


def users_articles(request, user_id):
    user = get_object_or_404(User, id=int(user_id))

    return render(request, 'blog/users_articles.html', {
        'articles': Article.objects.filter(user=user),
        'user': user,
    })
