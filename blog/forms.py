from django.forms import ModelForm
from blog.models import Article



class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = {'title', 'text', 'pdf_file'}


