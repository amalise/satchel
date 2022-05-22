from django.template import Library, loader
from django.http import QueryDict

from urllib.parse import urlparse, urlunparse

from satchel.core.models import Category, Tag

register = Library()


@register.inclusion_tag('blog/tags/blog_toc.html', takes_context = True)
def blog_toc(context):
    return {
        'request': context['request'],
        'index_page': context['index_page'],
        'blog_page': context['blog_page']
    }
    
@register.inclusion_tag('blog/tags/blog_summary.html', takes_context = True)
def blog_summary(context):
    return {
        'request': context['request'],
        'index_page': context['index_page'],
        'blog_page': context['blog_page']
    }

@register.inclusion_tag('blog/tags/category_list.html', takes_context = True)
def category_list(context):
    categories = context['index_page'].get_child_categories()
    return {
        'request': context['request'],
        'index_page': context['index_page'],
        'categories': categories
    }

@register.inclusion_tag('blog/tags/tag_list.html', takes_context = True)
def tag_list(context):
    tags = context['index_page'].get_child_tags()
    return {
        'request': context['request'],
        'index_page': context['index_page'],
        'tags': tags
    }
    
@register.inclusion_tag('blog/tags/search.html', takes_context = True)
def blog_search(context):
    return {
        'request': context['request'],
        'index_page': context['index_page'],
    }

@register.simple_tag()
def blog_date_slug_url(blog_page, index_page):
    date_published = blog_page.date_published
    url = index_page.full_url + index_page.reverse_subpage(
        'blog_by_date_slug',
        args = (
            date_published.year,
            "{0:02}".format(date_published.month),
            "{0:02}".format(date_published.day),
            blog_page.slug,
        )
    )
    return url

