from django.db import models

from modelcluster.fields import ParentalKey


from wagtail.core.models import Page

from wagtail.core.fields import RichTextField, StreamField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    ObjectList,
    PageChooserPanel,
    StreamFieldPanel,
    TabbedInterface,
)
from wagtail.images.edit_handlers import ImageChooserPanel


from satchel.core.blocks import ContentStreamBlock, PageStreamBlock


"""
    FlexPage

    A basic page, containing all the common content for pages in this site.
"""
class FlexPage(Page):
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
        StreamFieldPanel('page_content'),
    ]

    meta_panels = [
        MultiFieldPanel([
            FieldPanel('title'),
            ImageChooserPanel('image'),
            FieldPanel('abstract'),
        ], heading = 'Site navigation'),
        MultiFieldPanel([
            FieldPanel('banner_title'),
            FieldPanel('banner_subtitle'),
            ImageChooserPanel('banner_image'),
        ], heading = 'Banner content'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading = 'Content'),
        ObjectList(meta_panels, heading = 'Meta'),
        ObjectList(Page.promote_panels, heading = 'Promote'),
        ObjectList(Page.settings_panels, heading = 'Settings')
    ])

    def __str__(self):
        return self.title


"""
    HomePage

    A home page for the website.
"""
class HomePage(FlexPage):
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

    edit_handler = TabbedInterface([
        ObjectList(FlexPage.content_panels, heading = 'Content'),
        ObjectList(feature_panels, heading = 'Featured'),
        ObjectList(FlexPage.meta_panels, heading = 'Meta'),
        ObjectList(FlexPage.promote_panels, heading = 'Promote'),
        ObjectList(FlexPage.settings_panels, heading = 'Settings')
    ])

    def __str__(self):
        return self.title


"""
    FormPage

    A basic page which implements a web form.
"""
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

