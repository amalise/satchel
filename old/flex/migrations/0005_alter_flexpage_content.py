# Generated by Django 4.0.4 on 2022-05-01 10:25

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0004_alter_flexpage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='content',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a size'), ('h2', 'h2'), ('h3', 'h3'), ('h4', 'h4'), ('h5', 'h5'), ('h6', 'h6'), ('h7', 'h7')], required=False))])), ('paragraph', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(required=True))])), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alt_text', wagtail.core.blocks.TextBlock(required=True)), ('caption', wagtail.core.blocks.TextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))])), ('quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock(required=True)), ('attribution', wagtail.core.blocks.CharBlock(required=True)), ('citation_text', wagtail.core.blocks.CharBlock(required=False)), ('citation_link', wagtail.core.blocks.URLBlock(required=False))])), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='view', template='blocks/default_block.html'))], blank=True, verbose_name='Page content blocks.'),
        ),
    ]
