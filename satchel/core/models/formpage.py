from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.fields import RichTextField, StreamField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel

from satchel.core.blocks import ContentStreamBlock


class FormField(AbstractFormField):
    """
    Form element wrapper
    """
    page = ParentalKey(
        'FormPage',
        related_name = 'form_fields',
        on_delete = models.CASCADE,
    )


class FormPage(AbstractEmailForm):
    """
    A page which displays a form, which can be built in the Wagtail admin.
    """
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
    thank_you = RichTextField(
        blank = True,
        help_text = 'Content to display after form submission.'
    )

    content_panels = AbstractEmailForm.content_panels + [
        MultiFieldPanel([
            FieldPanel('subtitle'),
            ImageChooserPanel('image'),
        ], heading = 'Title section'),
        StreamFieldPanel('content'),
        InlinePanel('form_fields', label = 'Form fields'),
        FieldPanel('thank_you'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname = 'col6'),
                FieldPanel('to_address', classname = 'col6'),
            ]),
            FieldPanel('subject'),
        ], 'Email'),
    ]

