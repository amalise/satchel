from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet


@register_snippet
class Category(index.Indexed, models.Model):
    name = models.CharField(max_length = 255)
    slug = models.SlugField(unique = True, max_length = 80)

    panels = [
        FieldPanel('name'),
        FieldPanel('slug')
    ]

    search_fields = [
        index.SearchField('name')
    ]

    def get_slug(self):
        return self.slug

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

