"""
from django.db import models
from wagtail.core.fields import RichTextField, StreamField

from satchel.core.blocks import ContentStreamBlock, PageStreamBlock

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core.models import Page


class HomePage(Page):
    subtitle = models.TextField(
        max_length = 200,
        blank = True,
        help_text = 'Subtitle for the page header.',
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        related_name = '+',
        blank = True,
        null = True,
        help_text = 'Banner image for the page header.',
        on_delete = models.SET_NULL,
    )
    content = StreamField(
        ContentStreamBlock(),
        verbose_name = 'Page content blocks.',
        blank = True,
    )
    feature_title = models.CharField(
        max_length = 255,
        blank = True,
        help_text = 'Title for the featured content section.'
    )
    feature_limit = models.IntegerField(
        default = 4,
        blank = False,
        null = False,
        help_text = 'Max number of featured pages to display.'
    )
    feature_display = models.CharField(
        max_length = 20,
        default = 'card',
        choices = [('card', 'Cards'), ('list', 'List')],
        blank = True,
        null = True,
        help_text = 'Layout style for featured content.',
    )

    feature_pages = StreamField(
        PageStreamBlock(),
        verbose_name = 'Featured pages.',
        blank = True,
        null = True,
    )
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('subtitle'),
            ImageChooserPanel('image'),
        ], heading = 'Title section'),
        StreamFieldPanel('content'),
        MultiFieldPanel([
            FieldPanel('feature_title'),
            FieldPanel('feature_limit'),
            FieldPanel('feature_display'),
            StreamFieldPanel('feature_pages'),
        ], heading = 'Featured pages', classname = 'collapsible'),
    ]

    def __str__(self):
        return self.title

"""