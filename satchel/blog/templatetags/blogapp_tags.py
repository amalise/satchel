from django.template import Library, loader
from django.http import QueryDict

from urllib.parse import urlparse, urlunparse

from satchel.core.models import Category, Tag

register = Library()


@register.inclusion_tag('blog/tags/category_list.html', takes_context = True)
def category_list(context):
    categories = Category.objects.all()
    return {
        'request': context['request'],
        'blog_page': context['blog_page'],
        'categories': categories
    }

@register.inclusion_tag('blog/tags/tag_list.html', takes_context = True)
def tag_list(context):
    tags = Tag.objects.all()
    return {
        'request': context['request'],
        'blog_page': context['blog_page'],
        'tags': tags
    }

@register.simple_tag()
def post_page_date_slug_url(post_page, blog_page):
    date_published = post_page.date_published
    url = blog_page.full_url + blog_page.reverse_subpage(
        'post_by_date_slug',
        args = (
            date_published.year,
            "{0:02}".format(date_published.month),
            "{0:02}".format(date_published.day),
            post_page.slug,
        )
    )
    return url

