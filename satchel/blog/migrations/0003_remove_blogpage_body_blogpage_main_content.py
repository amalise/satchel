# Generated by Django 4.0.3 on 2022-04-04 01:14

from django.db import migrations
import streamfieldblocks.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpage_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='body',
        ),
        migrations.AddField(
            model_name='blogpage',
            name='main_content',
            field=wagtail.core.fields.StreamField([('title', streamfieldblocks.models.TitleBlock()), ('richtext', streamfieldblocks.models.SimpleRichTextBlock()), ('responsive_image', streamfieldblocks.models.ResponsiveImageBlock()), ('card', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.TextBlock()), ('page_link', wagtail.core.blocks.PageChooserBlock())])), ('text_with_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('position', wagtail.core.blocks.ChoiceBlock(choices=['left', 'right'])), ('richtext', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'ol', 'ul']))])), ('carousel', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())])), ('flush_list', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.TextBlock(help_text="List item's body text.")))]))], blank=True),
        ),
    ]