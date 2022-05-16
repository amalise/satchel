# Generated by Django 4.0.3 on 2022-04-12 06:41

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailcore', '0066_collection_management_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('subtitle', models.TextField(blank=True, help_text='Subtitle for page header.', max_length=200, null=True)),
                ('content', wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a size'), ('h2', 'h2'), ('h3', 'h3'), ('h4', 'h4'), ('h5', 'h5'), ('h6', 'h6'), ('h7', 'h7')], required=False))])), ('paragraph', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock())])), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alt_text', wagtail.core.blocks.CharBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.TextBlock(required=False))])), ('quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock()), ('attribution', wagtail.core.blocks.TextBlock(required=True)), ('citation', wagtail.core.blocks.URLBlock(required=False))])), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='view', template='blocks/embed_block.html'))], blank=True, verbose_name='Home content block')),
                ('banner_image', models.ForeignKey(blank=True, help_text='Banner image for page header.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]