#!usr/bin/env pyhton
# -*- coding: UTF-8 -*-
# Author:Yin
from django.urls import path, include

import blog.views


urlpatterns = [
    path('hello_world', blog.views.index),
    path('content', blog.views.article_content),
    path('', blog.views.get_index_page),
    # path('detail', blog.views.get_detail_page)
    path('detail/<int:article_id>', blog.views.get_detail_page)
]