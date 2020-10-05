from django.db import models

# Create your models here.
from django.db import models
from mdeditor.fields import MDTextField


class Article(models.Model):
    # 文章的唯一id
    article_id = models.AutoField(primary_key=True)
    # 文章标题
    title = models.TextField()
    # 文章主要内容
    # content = models.TextField()
    content = MDTextField()
    # 文章的摘要
    brief_content = models.TextField()
    # 文章的日期
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
