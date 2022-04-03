from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page


class HomePage(Page):
    # CLASS DATA
    hero_title = models.CharField(
        max_length = 120,
        blank = True,
        help_text = 'Main text displayed in the hero section.',
    )
    hero_subtitle = models.TextField(
        max_length = 200,
        blank = True,
        help_text = 'Subtitle following the main title in the hero section.',
    )
    action_button_text = models.CharField(
        max_length = 20,
        blank = True,
        default = 'Learn More',
        help_text = 'Action button text.',
    )
    action_button_link = models.ForeignKey(
        'wagtailcore.page',
        null = True,
        blank = True,
        related_name = "+",
        on_delete = models.SET_NULL,
        help_text = 'Internal page link when button is clicked.',
    )

    # ADMIN INTERFACE
    content_panels = Page.content_panels + [
        FieldPanel('hero_title'),
        FieldPanel('hero_subtitle'),
        FieldPanel('action_button_text'),
        PageChooserPanel('action_button_link'),
    ]

    # FUNCTION OVERRIDES

