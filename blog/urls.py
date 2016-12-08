from django.conf.urls import url
from blog import views


urlpatterns = [
    url(r'^$', 'blog.views.about', name='about'),
    url(r'^accounts/profile/$', views.CreateArticleView.as_view(), name='create_article'),
    url(r'^users/$', views.UserListView.as_view(), name='users_list'),
    url(r'^home/$', 'blog.views.home', name='home'),
    url(r'^site/$', 'blog.views.site', name='site'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', 'blog.views.show_article', name='article'),
    url(r'^user/(?P<user_id>[0-9]+)/articles/$', 'blog.views.users_articles', name='users_articles'),
]
