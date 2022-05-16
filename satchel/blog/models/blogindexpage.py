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
        context['blog_page'] = self

        paginator = Paginator(self.posts, 2)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.object_list.none()

        context['posts'] = posts
        return context

    def serve_preview(self, request, mode_name):
        return self.serve(request)

    def get_posts(self):
        return BlogPage.objects.descendant_of(self).live().order_by('-date_published')

    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            tags += post.get_tags()
        tags = sorted(set(tags))
        return tags

    @route(r'^tag/(?P<tag>[-\w]+)/$')
    def post_by_tag(self, request, tag):
        try:
            tag = Tag.objects.get(slug = tag)
        except Tag.DoesNotExist:
            if tag:
                msg = 'There are no blog posts tagged with "{}".'.format(tag)
                messages.add_message(request, messages.INFO, msg)
        self.posts = self.get_posts().filter(tags = tag)
        return self.render(request, context_overrides = { 'tag': tag })

    @route(r'^category/(?P<category>[-\w]+)/$')
    def post_by_category(self, request, category):
        try:
            category = Category.objects.get(slug = category)
        except Category.DoesNotExist:
            if tag:
                msg = 'There are no blog posts categorized in "{}".'.format(category)
                messages.add_message(request, messages.INFO, msg)
        self.posts = self.get_posts().filter(blog_category_relationship__category = category)
        return self.render(request, context_overrides = { 'category': category })

    @route(r'^$')
    def post_list(self, request):
        self.posts = self.get_posts()
        return self.render(request)

    @route(r'^(\d{4})/$')
    @route(r'^(\d{4})/(\d{2})/$')
    @route(r'^(\d{4})/(\d{2})/(\d{2})/$')
    def post_by_date(self, request, year, month = None, day = None):
        self.posts = self.get_posts().filter(date_published__year = year)
        if month:
            self.posts = self.posts.filter(date_published__month = month)
        if day:
            self.posts = self.posts.filter(date_published__day = day)
        return self.render(request)

    @route(r'^(\d{4})/(\d{2})/(\d{2})/(.+)/$')
    def post_by_date_slug(self, request, year, month, day, slug):
        post_page = self.get_posts().filter(slug = slug).first()
        if not post_page:
            raise Http404
        return post_page.serve(request)

