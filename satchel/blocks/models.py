from django.db import models

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleBlock(blocks.CharBlock):
    # ADMIN INTERFACE
    class Meta:
        template = 'blocks/title_block.html'


class SimpleRichTextBlock(blocks.StructBlock):
    #CLASS DATA
    richtext = blocks.RichTextBlock(features = ['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'ol', 'ul'])

    # ADMIN INTERFACE
    class Meta:
        icon = 'pilcrow'
        template = 'blocks/simple_richtext_block.html'


class ResponsiveImageBlock(ImageChooserBlock):
    # ADMIN INTERFACE
    class Meta:
        icon = 'image'
        template = 'blocks/responsive_image_block.html'


class CardBlock(blocks.StructBlock):
    # CLASS DATA
    image = ImageChooserBlock(required = False)
    title = blocks.CharBlock()
    body = blocks.TextBlock()
    page_link = blocks.PageChooserBlock()

    # ADMIN INTERFACE
    class Meta:
        icon = 'placeholder'
        template = 'blocks/card_block.html'


class RichTextImageBlock(blocks.StructBlock):
    # CLASS DATA
    image = ImageChooserBlock()
    position = blocks.ChoiceBlock(choices = [('left', 'Left'), ('right', 'Right')])
    richtext = blocks.RichTextBlock(features = ['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'ol', 'ul'])

    # ADMIN INTERFACE
    class Meta:
        icon = 'pilcrow'
        template = 'blocks/richtext_image_block.html'


class CarouselBlock(blocks.StreamBlock):
    # CLASS DATA
    image = ImageChooserBlock()

    # ADMIN INTERFACE
    class Meta:
        icon = 'cog'
        template = 'blocks/carousel_block.html'


class FlushListBlock(blocks.StructBlock):
    # CLASS DATA
    items = blocks.ListBlock(
        blocks.TextBlock(help_text = "List item's body text.")
    )

    # ADMIN INTERFACE
    class Meta:
        icon = 'list-ul'
        template = 'blocks/flush_list_block.html'


class TimelineBlock(blocks.StructBlock):
    # CLASS DATA
    title = blocks.CharBlock(max_length=100)
    text = blocks.TextBlock()
    date = blocks.DateBlock()

    # ADMIN INTERFACE
    class Meta:
        icon = "placeholder"
        template = "blocks/timeline_block.html"