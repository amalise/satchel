from django.db import models
from django.db.models import Q
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
from satchel.project.models import ProjectPage


class ProjectIndexPage(RoutablePageMixin, FlexPage):
    """
    Page which lists ProjectPages
    """
    subpage_types = ['ProjectPage']

    def get_context(self, request):
        context = super(ProjectIndexPage, self).get_context(request)
        context['index_page'] = self

        paginator = Paginator(self.projects, 10)
        page = request.GET.get('page')
        try:
            projects = paginator.page(page)
        except PageNotAnInteger:
            projects = paginator.page(1)
        except EmptyPage:
            projects = paginator.object_list.none()

        context['projects'] = projects
        return context

    def serve_preview(self, request, mode_name):
        return self.serve(request)

    def get_projects(self):
        return ProjectPage.objects.descendant_of(self).live().order_by('-date_updated')

    def get_child_tags(self):
        tags = []
        for project in self.get_projects():
            tags += project.get_tags()
        tags = sorted(set(tags))
        return tags

    def get_child_categories(self):
        categories = []
        for project in self.get_projects():
            categories += project.get_categories()
        categories = sorted(set(categories))
        return categories

    @route(r'^$')
    def project_list(self, request):
        self.projects = self.get_projects()
        return self.render(request)

    @route(r'^category/(?P<category>[-\w]+)/$')
    def project_by_category(self, request, category):
        self.search_type = 'category'
        self.search_term = category
        self.projects = self.get_projects().filter(project_category_relationship__category__slug = category)
        return self.render(request)

    @route(r'^tag/(?P<tag>[-\w]+)/$')
    def project_by_tag(self, request, tag):
        self.search_type = 'tag'
        self.search_term = tag
        self.projects = self.get_projects().filter(tags__slug = tag)
        return self.render(request)

    @route(r'^status/(?P<status>[-\w]+)/$')
    def project_by_status(self, request, status):
        self.search_type = 'status'
        self.search_term = status
        self.projects = self.get_projects().filter(project_category_relationship__status = category)
        return self.render(request)

    @route(r'^(\d{4})/$')
    @route(r'^(\d{4})/(\d{2})/$')
    @route(r'^(\d{4})/(\d{2})/(\d{2})/$')
    def project_by_date(self, request, year, month = None, day = None):
        self.search_type = 'date'
        self.search_term = year
        self.project = self.get_projects().filter(Q(date_updated__year = year) | Q(date_created__year = year))
        if month:
            df = DateFormat(datetime.date(int(year), int(month), 1))
            self.search_term = df.format('F Y')
            self.project = self.project.filter(Q(date_updated__month = month) | Q(date_created__month = month))
        if day:
            self.search_term = date_format(datetime.date(int(year), int(month), int(day)))
            self.project = self.project.filter(Q(date_updated__day = day) | Q(date_created__day = day))
        return self.render(request)

    @route(r'^(\d{4})/(\d{2})/(\d{2})/(.+)/$')
    def project_by_date_slug(self, request, year, month, day, slug):
        project_page = self.get_projects().filter(slug = slug).first()
        if not project_page:
            raise Http404
        return project_page.serve(request)

    @route(r'^search/$')
    def project_search(self, request):
        search_query = request.GET.get('q', None)
        self.projects = self.get_projects()
        if search_query:
            self.search_type = 'search'
            self.search_term = search_query
            self.projects = self.projects.search(search_query)
        return self.render(request)

