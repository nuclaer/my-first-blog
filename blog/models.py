# encoding: utf-8

from django.contrib.auth.models import User
from django.db import models

SHORT_TEXT_LEN = 250



class Article(models.Model):

    title = models.CharField(max_length=50, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    user = models.ForeignKey(User, blank=True, null=True)
    pdf_file = models.FileField(blank=True, null=True, verbose_name='Добавить файл')
    def __str__(self):
        return self.title

    def get_short_text(self):
        return self.text[:SHORT_TEXT_LEN]
