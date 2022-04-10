from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel

from blocks.models import RichTextImageBlock, BodyBlock


class FlexPage(Page):
    subtitle = models.CharField(
        max_length = 100,
        blank = True,
        null = True,
        help_text = 'Subtitle for page header.',
    )
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        blank = True,
        null = True,
        related_name = '+',
        help_text = 'Banner image for page header.',
        on_delete = models.SET_NULL,
    )
    content = StreamField(BodyBlock(), blank = True)

    # ADMIN
    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        ImageChooserPanel("banner_image"),
        StreamFieldPanel("content"),
    ]

