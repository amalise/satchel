from django.db import models
from wagtail.core.fields import StreamField
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from taggit.models import Tag as TaggitTag
from taggit.models import TaggedItemBase

from django import forms

#from wagtail.snippets.models import register_snippet
from blocks.models import (
    SimpleRichTextBlock,
    RichTextImageBlock,
)

from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from modelcluster.tags import ClusterTaggableManager

from wagtail.core.models import Page, Orderable

from wagtail.search import index


class BlogPage(Page):
    description = models.CharField(max_length = 255, blank = True)

    content_panels = Page.content_panels + [
        FieldPanel('description', classname = "full")
    ]

    def get_context(self, request):
        context = super().get_context(request)
        blogposts = self.get_children().live().order_by('-first_published_at')
        context['blogposts'] = blogposts
        return context


class PostPage(Page):
    header_image = models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete = models.SET_NULL,
        related_name = "+"
    )
    description = models.CharField(
        max_length = 255, 
        blank = True,
    )
    tags = ClusterTaggableManager(
        through = "blog.PostPageTag",
        blank = True,
    )
    categories = ParentalManyToManyField(
        'categories.Category',
        blank = True,
    )
    content = StreamField([
        ('paragraph', SimpleRichTextBlock()),
        ('image_paragraph', RichTextImageBlock()),
    ], blank = True)

    def main_image(self):
        if self.header_image:
            return self.header_image
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('description'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('header_image'),
            FieldPanel('description'),
            FieldPanel('tags'),
            FieldPanel('categories', widget = forms.CheckboxSelectMultiple),
        ], heading = "Post information"),
        StreamFieldPanel('content'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]


class PostGalleryImage(Orderable):
    page = ParentalKey(
        PostPage,
        on_delete=models.CASCADE,
        related_name='gallery_images',
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+',
    )
    caption = models.CharField(max_length = 150, blank = True)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


class PostPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'PostPage',
        related_name = "post_tags",
        on_delete = models.CASCADE
    )














"""
@register_snippet
class Tag(TaggitTag):
    class Meta:
        proxy = True


@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length = 255)
    slug = models.SlugField(unique = True, max_length = 80)

    # ADMIN
    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class PostPageBlogCategory(models.Model):
    page = ParentalKey(
        "blog.PostPage",
        on_delete = models.CASCADE,
        related_name = "categories"
    )
    blog_category = models.ForeignKey(
        "blog.BlogCategory",
        on_delete=models.CASCADE,
        related_name="post_pages"
    )

    # ADMIN
    panels = [
        SnippetChooserPanel("blog_category"),
    ]

    class Meta:
        unique_together = ("page", "blog_category")
"""
