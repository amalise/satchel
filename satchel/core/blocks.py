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
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
    URLBlock,
)
from wagtail.images.blocks import ImageChooserBlock


class HeadingBlock(StructBlock):
    text = CharBlock(required = True)
    size = ChoiceBlock(choices = [
        ('', 'Select a size'),
        ('h2', 'h2'),
        ('h3', 'h3'),
        ('h4', 'h4'),
        ('h5', 'h5'),
        ('h6', 'h6'),
        ('h7', 'h7'),
    ], blank = True, required = False)

    class Meta:
        icon = 'title'
        template = 'blocks/heading_block.html'


class ParagraphBlock(StructBlock):
    text = RichTextBlock()

    class Meta:
        icon = 'pilcrow'
        template = 'blocks/paragraph_block.html'


class ImageBlock(StructBlock):
    image = ImageChooserBlock(required = True)
    alt_text = CharBlock(required = True)
    caption = CharBlock(required = False)
    attribution = TextBlock(required = False)

    class Meta:
        icon = 'image'
        template = 'blocks/image_block.html'


class QuoteBlock(StructBlock):
    text = CharBlock()
    attribution = TextBlock(required = True)
    citation = URLBlock(required = False)

    class Meta:
        icon = 'openquote'
        template = 'blocks/quote_block.html'


class ContentStreamBlock(StreamBlock):
    heading = HeadingBlock()
    paragraph = ParagraphBlock()
    image = ImageBlock()
    quote = QuoteBlock()
    embed = EmbedBlock(
        icon = 'view',
        template = 'blocks/embed_block.html',
    )

