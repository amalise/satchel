from django.template import Library, loader
from django.http import QueryDict

from urllib.parse import urlparse, urlunparse

from satchel.core.models import Category, Tag

register = Library()


@register.inclusion_tag('project/tags/project_toc.html', takes_context = True)
def project_toc(context):
    return {
        'request': context['request'],
        'index_page': context['index_page'],
        'project_page': context['project_page']
    }
    
@register.inclusion_tag('project/tags/project_summary.html', takes_context = True)
def project_summary(context):
    return {
        'request': context['request'],
        'index_page': context['index_page'],
        'project_page': context['project_page']
    }

@register.inclusion_tag('project/tags/category_list.html', takes_context = True)
def category_list(context):
    categories = context['index_page'].get_child_categories()
    return {
        'request': context['request'],
        'index_page': context['index_page'],
        'categories': categories
    }

@register.inclusion_tag('project/tags/tag_list.html', takes_context = True)
def tag_list(context):
    tags = context['index_page'].get_child_tags()
    return {
        'request': context['request'],
        'index_page': context['index_page'],
        'tags': tags
    }

@register.inclusion_tag('project/tags/blog_list.html', takes_context = True)
def blog_list(context):
    tags = context['index_page'].get_child_tags()
    return {
        'request': context['request'],
        'index_page': context['index_page'],
        'project_page': context['project_page']
    }

@register.inclusion_tag('project/tags/search.html', takes_context = True)
def project_search(context):
    return {
        'request': context['request'],
        'index_page': context['index_page'],
    }

@register.simple_tag()
def project_date_slug_url(project_page, index_page):
    date_created = project_page.date_created
    url = index_page.full_url + index_page.reverse_subpage(
        'project_by_date_slug',
        args = (
            date_created.year,
            "{0:02}".format(date_created.month),
            "{0:02}".format(date_created.day),
            project_page.slug,
        )
    )
    return url

