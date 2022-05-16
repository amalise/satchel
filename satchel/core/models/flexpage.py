from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    ObjectList,
    StreamFieldPanel,
    TabbedInterface,
)
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from satchel.core.blocks import ContentStreamBlock


class FlexPage(Page):
    """
    Base Page Type

    This page contains all elements common to any page on the site:
        - title (Page):     Used in navigation
        - abstract:         Summary of the page
        - image:            Thumnail displayed when this page is listed elsewhere
        - banner elements:  Header banner, title, and sub-title
        - page_content:     Repeatable blocks of page content
    """
    abstract = RichTextField(
        blank = True,
        help_text = 'Summary of the page used by cards.'
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        related_name = '+',
        blank = True,
        null = True,
        help_text = 'Small image used by cards.',
        on_delete = models.SET_NULL,
    )
    banner_title = models.TextField(
        max_length = 200,
        blank = True,
        null = True,
        help_text = 'Title for the page header.',
    )
    banner_subtitle = models.TextField(
        max_length = 200,
        blank = True,
        null = True,
        help_text = 'Subtitle for the page header.',
    )
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        related_name = '+',
        blank = True,
        null = True,
        help_text = 'Banner image for the page header.',
        on_delete = models.SET_NULL,
    )
    page_content = StreamField(
        ContentStreamBlock(),
        verbose_name = 'Page content blocks.',
        blank = True
    )

    content_panels = [
        FieldPanel('title'),
        StreamFieldPanel('page_content'),
    ]

    meta_panels = [
        MultiFieldPanel([
            ImageChooserPanel('image'),
            FieldPanel('abstract'),
        ], heading = 'Site navigation'),
        MultiFieldPanel([
            FieldPanel('banner_title'),
            FieldPanel('banner_subtitle'),
            ImageChooserPanel('banner_image'),
        ], heading = 'Banner content'),
    ]

    promote_panels  = Page.promote_panels
    settings_panels = Page.settings_panels

    edit_handler = TabbedInterface([
        ObjectList(content_panels,  heading = 'Content'),
        ObjectList(meta_panels,     heading = 'Meta'),
        ObjectList(promote_panels,  heading = 'Promote'),
        ObjectList(settings_panels, heading = 'Settings')
    ])

    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('banner_title'),
        index.SearchField('banner_subtitle'),
        index.SearchField('abstract'),
        index.SearchField('page_content'),
    ]

    def __str__(self):
        return self.title

