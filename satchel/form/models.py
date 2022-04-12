from django.db import models

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.core.fields import RichTextField, StreamField

from satchel.core.blocks import ContentStreamBlock

from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core.models import Page


class FormField(AbstractFormField):
    page = ParentalKey(
        'FormPage',
        related_name = 'form_fields',
        on_delete = models.CASCADE,
    )


class FormPage(AbstractEmailForm):
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
        on_delete = models.SET_NULL,
    )
    content = StreamField(
        ContentStreamBlock(),
        verbose_name = 'Home content block',
        blank = True
    )
    thank_you = RichTextField(
        blank = True,
        help_text = 'Content to display after form submission.'
    )

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('subtitle'),
        ImageChooserPanel('banner_image'),
        StreamFieldPanel('content', classname = 'full'),
        InlinePanel('form_fields', label = 'Form fields'),
        FieldPanel('thank_you', classname = 'full')
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname = 'col6'),
                FieldPanel('to_address', classname = 'col6'),
            ])
            FieldPanel('subject'),
        ], 'Email'),
    ]

