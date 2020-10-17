from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Article

from django.core.paginator import Paginator
# Create your views here.


def index(request):
    return HttpResponse('hello world')


def article_content(request):
    article = Article.objects.all()[0]
    title = article.title
    brief_content = article.brief_content
    content = article.content
    article_id = article.article_id
    publish_date = article.publish_date
    return_str = 'title: %s , brief_content: %s, content: %s,article_id: %s, ' \
                 'publish_date: %s ' % (title, brief_content, content, article_id, publish_date)

    return HttpResponse(return_str)


def get_index_page(request):
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1

    all_article = Article.objects.all()
    top5_article_list = Article.objects.order_by('-publish_date')[:5]

    paginator = Paginator(all_article, 5)
    page_num = paginator.num_pages
    page_detail_list = paginator.page(page)
    if page_detail_list.has_next():
        next_page = page + 1
    else:
        next_page = page
    if page_detail_list.has_previous():
        precious_page = page - 1
    else:
        precious_page = page

    return render(request, 'blog/index.html', {
                            'article_list': page_detail_list,
                            'page_num': range(1, page_num + 1),
                            'next_page': next_page,
                            'precious_page': precious_page,
                            'top5_article_list': top5_article_list

                       }
                  )


def get_detail_page(request, article_id):
    all_article = Article.objects.all()
    curr_article = None
    previous_index = 0
    next_index = 0
    previous_article = None
    next_article = None

    for index, article in enumerate(all_article):
        first_flag = None
        last_flag = None

        # 首页
        if index == 0:
            previous_index = 0
            next_index = index + 1
            first_flag = 1

        # 末页
        elif index == len(all_article) - 1:
            previous_index = index - 1
            next_index = index
            last_flag = 1
        else:
            previous_index = index - 1
            next_index = index + 1

        if article.article_id == article_id:
            curr_article = article
            previous_article = all_article[previous_index]
            if len(all_article) != 1:
                next_article = all_article[next_index]
            break

    # curr_article = Article.objects.all()[0]
    # section_list = curr_article.content.split('\n')
    section_list = curr_article.content
    return render(request, 'blog/detail.html', {
        'curr_article': curr_article,
        'section_list': section_list,
        'previous_article': previous_article,
        'next_article': next_article,
        'first_flag': first_flag,
        'last_flag': last_flag,
    })

