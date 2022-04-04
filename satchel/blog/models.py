from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel


class BlogIndexPage(Page):
    # CLASS DATA
    background_image = models.ForeignKey(
        'wagtailimages.Image',
        blank = False,
        null = True,
        related_name = '+',
        help_text = 'Header background image.',
        on_delete = models.SET_NULL,
    )
    headline_text = models.CharField(
        max_length = 70,
        blank = True, 
        help_text = 'Blog listing page header text.',
    )

    # ADMIN INTERFACE
    content_panels = Page.content_panels + [
        ImageChooserPanel('background_image'),
        FieldPanel('headline_text'),
    ]
    subpage_types = ['blog.BlogPage']

    # FUNCTION OVERRIDES
    # Add list of only published posts, in reverse chronological order
    def get_context(self, request):
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('first_published_at')
        context['blogpages'] = blogpages
        return context


class BlogPage(Page):
    # CLASS DATA
    date = models.DateField('Article Date')
    intro = models.TextField('Introduction')
    body = RichTextField(blank = True)
    featured = models.BooleanField(default = False)

    # ADMIN INTERFACE
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('featured'),
        FieldPanel('intro'),
        FieldPanel('body', classname = 'full'),
    ]
