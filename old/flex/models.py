"""
from django.db import models
from wagtail.core.fields import RichTextField, StreamField

from satchel.core.blocks import ContentStreamBlock

from wagtail.admin.edit_handlers import (
    FieldPanel,
    StreamFieldPanel,
    MultiFieldPanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core.models import Page


class FlexPage(Page):
    subtitle = models.TextField(
        max_length = 200,
        blank = True,
        null = True,
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
        blank = True
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('subtitle'),
            ImageChooserPanel('image'),
        ], heading = 'Title section'),
        StreamFieldPanel('content'),
    ]

    def __str__(self):
        return self.title

"""