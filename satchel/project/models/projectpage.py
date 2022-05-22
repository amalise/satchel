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

from satchel.core.models import FlexPage


class ProjectPersonRelationship(Orderable, models.Model):
    """
    Database table to store ProjectPage <-> Person data
    """
    project = ParentalKey(
        'ProjectPage',
        related_name = 'project_person_relationship',
        on_delete = models.CASCADE,
    )
    person = models.ForeignKey(
        'core.Person',
        related_name = 'person_project_relationship',
        on_delete = models.CASCADE,
    )

    panels = [
        SnippetChooserPanel('person')
    ]

    class Meta:
        unique_together = ('project', 'person')


class ProjectCategoryRelationship(Orderable, models.Model):
    """
    Database table to store ProjectPage <-> Category data
    """
    project = ParentalKey(
        'ProjectPage',
        related_name = 'project_category_relationship',
        on_delete = models.CASCADE,
    )
    category = models.ForeignKey(
        'core.Category',
        related_name = 'category_project_relationship',
        on_delete = models.CASCADE,
    )

    panels = [
        SnippetChooserPanel('category')
    ]

    class Meta:
        unique_together = ('project', 'category')



class ProjectTagRelationship(TaggedItemBase):
    """
    Tag interface for project pages
    """
    content_object = ParentalKey(
        'ProjectPage',
        related_name = 'project_tag_relationship',
        on_delete = models.CASCADE
    )


class ProjectPage(FlexPage):
    """
    A project page

    Uses FlexPage for core content, adding
        - collaborators
        - creation date
        - update date
        - project status
        - categories
        - tags
    """
    date_created = models.DateField(
        blank = True,
        null = True,
        default = datetime.today,
        help_text = 'Date of project inception.'
    )
    date_updated = models.DateField(
        blank = True,
        null = True,
        default = datetime.today,
        help_text = 'Date of last status change.'
    )
    status = models.CharField(
        max_length = 20,
        default = 'new',
        choices = [
            ('new', 'New Idea'),
            ('research', 'Research'),
            ('active', 'Active'),
            ('idle', 'Idle'),
            ('complete', 'Complete'),
            ('archive', 'Archived'),
            ('abandon', 'Abandoned'),
        ],
        blank = False,
        null = False,
        help_text = 'Current project status.'

    )
    tags = ClusterTaggableManager(
        through = ProjectTagRelationship,
        blank = True
    )

    project_panels = [
        MultiFieldPanel([
            InlinePanel(
                'project_person_relationship',
                label = 'collaborators',
                min_num = 1,
            ),
            FieldPanel('date_created'),
            FieldPanel('date_updated'),
            FieldPanel('status'),
        ], heading = 'Publication'),
        MultiFieldPanel([
            InlinePanel(
                'project_category_relationship',
                label = 'categories',
                min_num = 1,
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
        ObjectList(project_panels,  heading = 'Project'),
        ObjectList(gallery_panels,  heading = 'Gallery'),
        ObjectList(meta_panels,     heading = 'Meta'),
        ObjectList(promote_panels,  heading = 'Promote'),
        ObjectList(settings_panels, heading = 'Settings')
    ])

    parent_page_types = ['ProjectIndexPage']
    subpage_types = []

    def get_context(self, request):
        context = super().get_context(request)
        context['index_page'] = self.get_parent().specific
        context['project_page'] = self
        return context

    def collaborators(self):
        collaborators = [
            n.person for n in self.project_person_relationship.all()
        ]
        return collaborators

    def categories(self):
        categories = [
            n.category for n in self.project_category_relationship.all()
        ]
        return categories

    def blogs(self):
        blogs = [
            n.blog for n in self.project_blog_relationship.all()
        ]
        return blogs

    def get_tags(self):
        tags = self.tags.all()
        for tag in tags:
            tag.url = '/' + '/'.join(s.strip('/') for s in [
                self.get_parent().url,
                'tags',
                tag.slug
            ])
        return tags

    def get_categories(self):
        categories = self.categories()
        for category in categories:
            category.url = '/' + '/'.join(s.strip('/') for s in [
                self.get_parent().url,
                'categories',
                category.slug
            ])
        return categories

    @cached_property
    def project_page(self):
        return self.get_parent().specific

    @cached_property
    def canonical_url(self):
        from satchel.project.templatetags.project_tags import project_date_slug_url

        return project_date_slug_url(self, self.get_parent().specific)

