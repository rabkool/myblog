#!usr/bin/env pyhton
# -*- coding: UTF-8 -*-
# Author:Yin
from django.urls import path, include
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

import blog.views

urlpatterns = [
    path('hello_world', blog.views.index),
    path('content', blog.views.article_content),
    path('', blog.views.get_index_page),
    # path('detail', blog.views.get_detail_page)
    path('detail/<int:article_id>', blog.views.get_detail_page),
    url(r'mdeditor/', include('mdeditor.urls')),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
