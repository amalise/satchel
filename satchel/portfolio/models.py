from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from blocks.models import TimelineBlock


class PortfolioPage(Page):
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
    experience = StreamField([
        ('timeline_block', TimelineBlock()),
    ], null=True, blank=True)

    # ADMIN INTERFACE
    content_panels = Page.content_panels + [
        ImageChooserPanel('background_image'),
        FieldPanel('headline_text'),
        StreamFieldPanel('experience'),
    ]
    subpage_types = ['portfolio.ProjectPage']

    # FUNCTION OVERRIDES
    def get_context(self, request):
        context = super().get_context(request)
        project_pages = self.get_children().live().order_by('-first_published_at')
        context['project_pages'] = project_pages
        return context


class ProjectPage(Page):
    # CLASS DATA
    project_title = models.CharField(
        max_length = 150
    )
    date = models.DateField('Article Date')
    image = models.ForeignKey(
        'wagtailimages.Image',
        blank = False,
        null = True,
        related_name = '+',
        help_text = 'Project Image',
        on_delete = models.SET_NULL,
    )
    intro = models.TextField()
    testimonials = models.ForeignKey(
        'snippets.Testimonial', 
        on_delete = models.SET_NULL, 
        related_name = '+',
        help_text = "Project Testimonials",
        blank = True,
        null = True,
    )

    # ADMIN INTERFACE
    content_panels = Page.content_panels + [
        FieldPanel('project_title'),
        FieldPanel('date'),
        ImageChooserPanel('image'),
        FieldPanel('intro'),
        SnippetChooserPanel('testimonials'),
    ]

    # FUNCTION OVERRIDES
