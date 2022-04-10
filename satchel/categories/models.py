from django.db import models

from wagtail.core.models import Page
from wagtail.snippets.models import register_snippet

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


@register_snippet
class Category(models.Model):
    name = models.CharField(max_length = 255)
    slug = models.SlugField(
        unique = True,
        max_length = 80
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null = True,
        blank = True,
        on_delete = models.SET_NULL,
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class CategoryIndexPage(Page):
    def get_context(self, request):
        context = super().get_context(request)

        category = request.GET.get('category')
        blogposts = PostPage.objects.filter(categories__name=category)
        context['blobposts'] = blogposts

        return context

