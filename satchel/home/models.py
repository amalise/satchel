from django.db import models
from wagtail.core.fields import RichTextField, StreamField

from satchel.core.blocks import ContentStreamBlock

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core.models import Page


class HomePage(Page):
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        blank = True,
        null = True,
        related_name = '+',
        help_text = 'Banner image for the hero section.',
        on_delete = models.SET_NULL,
    )
    hero_title = models.TextField(
        max_length = 120,
        blank = True,
        help_text = 'Main title for the hero section',
    )
    hero_subtitle = models.TextField(
        max_length = 200,
        blank = True,
        help_text = 'Subtitle for the hero section.',
    )
    cta_button_text = models.TextField(
        max_length = 20,
        blank = True,
        default = 'Learn More',
        help_text = 'Hero section button text.',
    )
    cta_button_link = models.ForeignKey(
        'wagtailcore.page',
        related_name = '+',
        null = True,
        blank = True,
        on_delete = models.SET_NULL,
        help_text = 'Internal page linked when hero button is clicked.'
    )
    content = StreamField(
        ContentStreamBlock(),
        verbose_name = 'Home content block',
        blank = True
    )
    feature_title = models.TextField(
        max_length = 255,
        blank = True,
        help_text = 'Title for the featured content section.'
    )
    feature_pages = models.ForeignKey(
        'wagtailcore.page',
        related_name = '+',
        null = True,
        blank = True,
        on_delete = models.SET_NULL,
        help_text = 'Pages to display in the featured content section.',
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('hero_image'),
            FieldPanel('hero_title'),
            FieldPanel('hero_subtitle'),
            MultiFieldPanel([
                FieldPanel('cta_button_text'),
                PageChooserPanel('cta_button_link'),
            ]),
        ], heading = 'Hero section'),
        StreamFieldPanel('content', classname = 'full'),
        MultiFieldPanel([
            FieldPanel('feature_title'),
            PageChooserPanel('feature_pages'),
        ], heading = 'Featured content', classname = 'collapsible')
    ]

    def __str__(self):
        return self.title

