from django.db import models

from modelcluster.models import ClusterableModel

from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    MultiFieldPanel,
    PageChooserPanel,
)

from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet

'''

@register_snippet
class Person(index.Indexed, ClusterableModel):
    first_name = models.CharField('First name', max_length = 200)
    last_name = models.CharField('Last name', max_length = 200)
    job_title = models.CharField('Job title', max_length = 200)

    image = models.ForeignKey(
        'wagtailimages.Image',
        null = True,
        blank = True,
        on_delete = models.SET_NULL,
        related_name = '+'
    )

    panels = [
        MultipleFieldPanel([
            FieldRowPanel([
                FieldPanel('first_name',  classname = 'col-6'),
                FieldPanel('last_name',   classname = 'col-6'),

            ])
        ], "Name"),
        FieldPanel('job_title'),
        ImageChooserPanel('image'),
    ]

    search_fields = [
        index.SearchField('first_name'),
        index.SearchField('last_name')
    ]

    @property
    def thumb_image(self):
        try:
            return self.image.get_rendition('fill-50x50').img_tag()
        except:
            return ''

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'

'''