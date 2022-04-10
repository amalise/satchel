from django.db import models

from wagtail.core.blocks import (
    BooleanBlock,
    CharBlock,
    ChoiceBlock,
    DateTimeBlock,
    FieldBlock,
    IntegerBlock,
    ListBlock,
    PageChooserBlock,
    RawHTMLBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    StructValue,
    TextBlock,
    URLBlock,
)
from wagtail.images.blocks import ImageChooserBlock


class SimpleRichTextBlock(StructBlock):
    text = RichTextBlock()

    class Meta:
        icon = 'pilcrow'
        template = 'blocks/simple_richtext_block.html'


class RichTextImageBlock(StructBlock):
    reverse = BooleanBlock(required = False)
    text = RichTextBlock()
    image = ImageChooserBlock()

    # ADMIN
    class Meta:
        icon = 'doc-empty'
        template = 'blocks/richtext_image_block.html'

