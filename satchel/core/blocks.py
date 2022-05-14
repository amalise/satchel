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
from wagtail.embeds.blocks import EmbedBlock
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
    text = RichTextBlock(required = True)

    class Meta:
        icon = 'pilcrow'
        template = 'blocks/paragraph_block.html'


class ImageBlock(StructBlock):
    image = ImageChooserBlock(required = True)
    alt_text = TextBlock(required = True)
    caption = TextBlock(required = False)
    attribution = CharBlock(required = False)

    class Meta:
        icon = 'image / picture'
        template = 'blocks/image_block.html'


class QuoteBlock(StructBlock):
    text = TextBlock(required = True)
    attribution = CharBlock(required = True)
    citation_text = CharBlock(required = False)
    citation_link = URLBlock(required = False)

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
        template = 'blocks/default_block.html',
    )


class PageStreamBlock(StreamBlock):
    page = PageChooserBlock()

    class Meta:
        icon = 'doc-full'
        template = 'blocks/default_block.html'

