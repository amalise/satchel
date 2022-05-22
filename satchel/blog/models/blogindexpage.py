from django.db import models
from django.contrib import messages
from django.shortcuts import redirect, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey

from taggit.models import Tag, TaggedItemBase

from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.admin.edit_handlers import (
    MultiFieldPanel,
    FieldPanel,
    InlinePanel,
    ObjectList,
    TabbedInterface,
)
from wagtail.core.models import Orderable
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from satchel.core.models import FlexPage, Category, Tag
from satchel.blog.models import BlogPage


class BlogIndexPage(RoutablePageMixin, FlexPage):
    """
    Page which lists BlogPages
    """
    subpage_types = ['BlogPage']

    def get_context(self, request):
        context = super(BlogIndexPage, self).get_context(request)
        context['index_page'] = self

        paginator = Paginator(self.blogs, 10)
        page = request.GET.get('page')
        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.object_list.none()

        context['blogs'] = blogs
        return context

    def serve_preview(self, request, mode_name):
        return self.serve(request)

    def get_blogs(self):
        return BlogPage.objects.descendant_of(self).live().order_by('-date_published')

    def get_child_tags(self):
        tags = []
        for blog in self.get_blogs():
            tags += blog.get_tags()
        tags = sorted(set(tags))
        return tags

    def get_child_categories(self):
        categories = []
        for blog in self.get_blogs():
            categories += blog.get_categories()
        categories = sorted(set(categories))
        return categories

    @route(r'^$')
    def blog_list(self, request):
        self.blogs = self.get_blogs()
        return self.render(request)

    @route(r'^category/(?P<category>[-\w]+)/$')
    def blog_by_category(self, request, category):
        self.search_type = 'category'
        self.search_term = category
        self.blogs = self.get_blogs().filter(blog_category_relationship__category__slug = category)
        return self.render(request)

    @route(r'^tag/(?P<tag>[-\w]+)/$')
    def blog_by_tag(self, request, tag):
        self.search_type = 'tag'
        self.search_term = tag
        self.blogs = self.get_blogs().filter(tags__slug = tag)
        return self.render(request)

    @route(r'^(\d{4})/$')
    @route(r'^(\d{4})/(\d{2})/$')
    @route(r'^(\d{4})/(\d{2})/(\d{2})/$')
    def blog_by_date(self, request, year, month = None, day = None):
        self.search_type = 'date'
        self.search_term = year
        self.blogs = self.get_blogs().filter(date_published__year = year)
        if month:
            df = DateFormat(datetime.date(int(year), int(month), 1))
            self.search_term = df.format('F Y')
            self.blogs = self.blogs.filter(date_published__month = month)
        if day:
            self.search_term = date_format(datetime.date(int(year), int(month), int(day)))
            self.blogs = self.blogs.filter(date_published__day = day)
        return self.render(request)

    @route(r'^(\d{4})/(\d{2})/(\d{2})/(.+)/$')
    def blog_by_date_slug(self, request, year, month, day, slug):
        blog_page = self.get_blogs().filter(slug = slug).first()
        if not blog_page:
            raise Http404
        return blog_page.serve(request)

    @route(r'^search/$')
    def blog_search(self, request):
        search_query = request.GET.get('q', None)
        self.blogs = self.get_blogs()
        if search_query:
            self.search_type = 'search'
            self.search_term = search_query
            self.blogs = self.blogs.search(search_query)
        return self.render(request)

