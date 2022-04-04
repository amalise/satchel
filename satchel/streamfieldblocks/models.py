from django.db import models


from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleBlock(blocks.CharBlock):
    # ADMIN INTERFACE
    class Meta:
        template = 'streamfieldblocks/title_block.html'


class SimpleRichTextBlock(blocks.StructBlock):
    #CLASS DATA
    richtext = blocks.RichTextBlock(features = ['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'ol', 'ul'])

    # ADMIN INTERFACE
    class Meta:
        icon = 'pilcrow'
        template = 'streamfieldblocks/simple_richtext_block.html'


class ResponsiveImageBlock(ImageChooserBlock):
    # ADMIN INTERFACE
    class Meta:
        icon = 'image'
        template = 'streamfieldblocks/responsive_image_block.html'


class CardBlock(blocks.StructBlock):
    # CLASS DATA
    image = ImageChooserBlock(required = False)
    title = blocks.CharBlock()
    body = blocks.TextBlock()
    page_link = blocks.PageChooserBlock()

    # ADMIN INTERFACE
    class Meta:
        icon = 'placeholder'
        template = 'streamfieldblocks/card_block.html'


class RichTextImageBlock(blocks.StructBlock):
    # CLASS DATA
    image = ImageChooserBlock()
    position = blocks.ChoiceBlock(choices = [('left', 'Left'), ('right', 'Right')])
    richtext = blocks.RichTextBlock(features = ['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'ol', 'ul'])

    # ADMIN INTERFACE
    class Meta:
        icon = 'pilcrow'
        template = 'streamfieldblocks/richtext_image_block.html'


class CarouselBlock(blocks.StreamBlock):
    # CLASS DATA
    image = ImageChooserBlock()

    # ADMIN INTERFACE
    class Meta:
        icon = 'cog'
        template = 'streamfieldblocks/carousel_block.html'


class FlushListBlock(blocks.StructBlock):
    # CLASS DATA
    items = blocks.ListBlock(
        blocks.TextBlock(help_text = "List item's body text.")
    )

    # ADMIN INTERFACE
    class Meta:
        icon = 'list-ul'
        template = 'streamfieldblocks/flush_list_block.html'

