from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Orderable
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class FlexPageGalleryImage(Orderable):
    page = ParentalKey(
        'FlexPage',
        on_delete = models.CASCADE,
        related_name = 'gallery_images'
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete = models.CASCADE,
        related_name = '+'
    )
    caption = models.CharField(blank = True, max_length = 250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption')
    ]