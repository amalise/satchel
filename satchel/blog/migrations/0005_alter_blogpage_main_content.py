# Generated by Django 4.0.3 on 2022-04-04 02:16

import blocks.models
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blogpage_main_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='main_content',
            field=wagtail.core.fields.StreamField([('title', blocks.models.TitleBlock()), ('richtext', wagtail.core.blocks.StructBlock([('richtext', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'ol', 'ul']))])), ('responsive_image', blocks.models.ResponsiveImageBlock()), ('card', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.TextBlock()), ('page_link', wagtail.core.blocks.PageChooserBlock())])), ('text_with_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('position', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')])), ('richtext', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'ol', 'ul']))])), ('carousel', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())])), ('flush_list', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.TextBlock(help_text="List item's body text.")))]))], blank=True),
        ),
    ]