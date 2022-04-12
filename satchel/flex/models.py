from django.db import models
from wagtail.core.fields import RichTextField, StreamField

from satchel.core.blocks import ContentStreamBlock

from wagtail.admin.edit_handlers import (
    FieldPanel,
    StreamFieldPanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core.models import Page


class FlexPage(Page):
    subtitle = models.TextField(
        max_length = 200,
        blank = True,
        null = True,
        help_text = 'Subtitle for page header.',
    )
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        related_name = '+',
        blank = True,
        null = True,
        help_text = 'Banner image for page header.',
        on_delete = models.SET_NULL,
    )
    content = StreamField(
        ContentStreamBlock(),
        verbose_name = 'Home content block',
        blank = True
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        ImageChooserPanel('banner_image'),
        StreamFieldPanel('content', classname = 'full'),
    ]

    def __str__(self):
        return self.title

