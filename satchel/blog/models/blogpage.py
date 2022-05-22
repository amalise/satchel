from django.db import models
from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.functional import cached_property

from datetime import datetime

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
from wagtail.admin.edit_handlers import PageChooserPanel

from satchel.core.models import FlexPage


class BlogPersonRelationship(Orderable, models.Model):
    """
    Database table to store BlogPage <-> Person data
    """
    blog = ParentalKey(
        'BlogPage',
        related_name = 'blog_person_relationship',
        on_delete = models.CASCADE,
    )
    person = models.ForeignKey(
        'core.Person',
        related_name = 'person_blog_relationship',
        on_delete = models.CASCADE,
    )

    panels = [
        SnippetChooserPanel('person')
    ]

    class Meta:
        unique_together = ('blog', 'person')


class BlogProjectRelationship(Orderable, models.Model):
    """
    Database table to store BlogPage <-> Project data
    """
    blog = ParentalKey(
        'BlogPage',
        related_name = 'blog_project_relationship',
        on_delete = models.CASCADE,
    )
    project = models.ForeignKey(
        'project.ProjectPage',
        related_name = 'project_blog_relationship',
        on_delete = models.CASCADE,
    )

    panels = [
        PageChooserPanel('project', 'project.ProjectPage')
    ]

    class Meta:
        unique_together = ('blog', 'project')


class BlogCategoryRelationship(Orderable, models.Model):
    """
    Database table to store BlogPage <-> Category data
    """
    blog = ParentalKey(
        'BlogPage',
        related_name = 'blog_category_relationship',
        on_delete = models.CASCADE,
    )
    category = models.ForeignKey(
        'core.Category',
        related_name = 'category_blog_relationship',
        on_delete = models.CASCADE,
    )

    panels = [
        SnippetChooserPanel('category')
    ]

    class Meta:
        unique_together = ('blog', 'category')



class BlogTagRelationship(TaggedItemBase):
    """
    Tag interface for blog pages
    """
    content_object = ParentalKey(
        'BlogPage',
        related_name = 'blog_tag_relationship',
        on_delete = models.CASCADE
    )


class BlogPage(FlexPage):
    """
    A blog page

    Uses FlexPage for core content, adding
        - authors
        - publication date
        - categories
        - tags
    """
    date_published = models.DateField(
        blank = True,
        null = True,
        default = datetime.today,
        help_text = 'Date blog post published.'
    )
    tags = ClusterTaggableManager(
        through = BlogTagRelationship,
        blank = True
    )
    previous_blog = models.ForeignKey(
        'self',
        blank = True,
        null = True,
        on_delete = models.SET_NULL,
        help_text = 'Previous blog post.'
    )

    blog_panels = [
        MultiFieldPanel([
            InlinePanel(
                'blog_person_relationship',
                label = 'authors',
                min_num = 1,
            ),
            FieldPanel('date_published'),
        ], heading = 'Publication'),
        MultiFieldPanel([
            InlinePanel(
                'blog_project_relationship',
                label = 'projects',
            ),
            PageChooserPanel('previous_blog', 'blog.BlogPage'),
        ], heading = 'Relationships'),
        MultiFieldPanel([
            InlinePanel(
                'blog_category_relationship',
                label = 'categories',
            ),
            FieldPanel('tags'),
        ], heading = 'Filing'),
    ]

    content_panels  = FlexPage.content_panels
    gallery_panels  = FlexPage.gallery_panels
    meta_panels     = FlexPage.meta_panels
    promote_panels  = FlexPage.promote_panels
    settings_panels = FlexPage.settings_panels

    edit_handler = TabbedInterface([
        ObjectList(content_panels,  heading = 'Content'),
        ObjectList(blog_panels,     heading = 'Blog'),
        ObjectList(gallery_panels,  heading = 'Gallery'),
        ObjectList(meta_panels,     heading = 'Meta'),
        ObjectList(promote_panels,  heading = 'Promote'),
        ObjectList(settings_panels, heading = 'Settings')
    ])

    parent_page_types = ['BlogIndexPage']
    subpage_types = []

    def get_context(self, request):
        context = super().get_context(request)
        context['index_page'] = self.get_parent().specific
        context['blog_page'] = self
        return context

    def authors(self):
        authors = [
            n.person for n in self.blog_person_relationship.all()
        ]
        return authors

    def projects(self):
        projects = [
            n.project for n in self.blog_project_relationship.all()
        ]
        return projects

    def categories(self):
        categories = [
            n.category for n in self.blog_category_relationship.all()
        ]
        return categories

    def get_categories(self):
        categories = self.categories()
        for category in categories:
            category.url = '/' + '/'.join(s.strip('/') for s in [
                self.get_parent().url,
                'categories',
                category.slug
            ])
        return categories

    def get_tags(self):
        tags = self.tags.all()
        for tag in tags:
            tag.url = '/' + '/'.join(s.strip('/') for s in [
                self.get_parent().url,
                'tags',
                tag.slug
            ])
        return tags

    def next_blogs(self):
        blogs = BlogPage.objects.all().live().filter(previous_blog = self)
        return blogs

    @cached_property
    def blog_page(self):
        return self.get_parent().specific

    @cached_property
    def canonical_url(self):
        from satchel.blog.templatetags.blog_tags import blog_date_slug_url

        return blog_date_slug_url(self, self.get_parent().specific)

