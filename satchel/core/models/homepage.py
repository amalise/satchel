from django.db import models

from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    ObjectList,
    StreamFieldPanel,
    TabbedInterface,
)

from satchel.core.blocks import PageStreamBlock
from satchel.core.models import FlexPage


class HomePage(FlexPage):
    """
    A site homepage

    Adds a list of featured pages from the site.
    """
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

    feature_panels = [
         MultiFieldPanel([
            FieldPanel('feature_title'),
            FieldPanel('feature_limit'),
            FieldPanel('feature_display'),
            StreamFieldPanel('feature_pages'),
        ], heading = 'Featured pages'),
    ]

    content_panels  = FlexPage.content_panels
    meta_panels     = FlexPage.meta_panels
    promote_panels  = FlexPage.promote_panels
    settings_panels = FlexPage.settings_panels

    edit_handler = TabbedInterface([
        ObjectList(content_panels,  heading = 'Content'),
        ObjectList(feature_panels,  heading = 'Featured'),
        ObjectList(meta_panels,     heading = 'Meta'),
        ObjectList(promote_panels,  heading = 'Promote'),
        ObjectList(settings_panels, heading = 'Settings')
    ])

    def __str__(self):
        return self.title

