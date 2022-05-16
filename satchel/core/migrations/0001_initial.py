# Generated by Django 4.0.4 on 2022-05-15 18:39

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtail.search.index


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('wagtailimages', '0023_add_choose_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=80, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
        migrations.CreateModel(
            name='FlexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('abstract', wagtail.core.fields.RichTextField(blank=True, help_text='Summary of the page used by cards.')),
                ('banner_title', models.TextField(blank=True, help_text='Title for the page header.', max_length=200, null=True)),
                ('banner_subtitle', models.TextField(blank=True, help_text='Subtitle for the page header.', max_length=200, null=True)),
                ('page_content', wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a size'), ('h2', 'h2'), ('h3', 'h3'), ('h4', 'h4'), ('h5', 'h5'), ('h6', 'h6'), ('h7', 'h7')], required=False))])), ('paragraph', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(required=True))])), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alt_text', wagtail.core.blocks.TextBlock(required=True)), ('caption', wagtail.core.blocks.TextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))])), ('quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock(required=True)), ('attribution', wagtail.core.blocks.CharBlock(required=True)), ('citation_text', wagtail.core.blocks.CharBlock(required=False)), ('citation_link', wagtail.core.blocks.URLBlock(required=False))])), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='view', template='blocks/default_block.html'))], blank=True, verbose_name='Page content blocks.')),
                ('banner_image', models.ForeignKey(blank=True, help_text='Banner image for the page header.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('image', models.ForeignKey(blank=True, help_text='Small image used by cards.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('flexpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.flexpage')),
                ('feature_title', models.CharField(blank=True, help_text='Title for the featured content section.', max_length=255)),
                ('feature_limit', models.IntegerField(default=4, help_text='Max number of featured pages to display.')),
                ('feature_display', models.CharField(blank=True, choices=[('card', 'Cards'), ('list', 'List')], default='card', help_text='Layout style for featured content.', max_length=20, null=True)),
                ('feature_pages', wagtail.core.fields.StreamField([('page', wagtail.core.blocks.PageChooserBlock())], blank=True, null=True, verbose_name='Featured pages.')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.flexpage',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='First name')),
                ('last_name', models.CharField(max_length=200, verbose_name='Last name')),
                ('job_title', models.CharField(max_length=200, verbose_name='Job title')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'people',
            },
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
        migrations.CreateModel(
            name='FormPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('to_address', models.CharField(blank=True, help_text='Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.', max_length=255, verbose_name='to address')),
                ('from_address', models.CharField(blank=True, max_length=255, verbose_name='from address')),
                ('subject', models.CharField(blank=True, max_length=255, verbose_name='subject')),
                ('subtitle', models.TextField(blank=True, help_text='Subtitle for the page header.', max_length=200, null=True)),
                ('content', wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a size'), ('h2', 'h2'), ('h3', 'h3'), ('h4', 'h4'), ('h5', 'h5'), ('h6', 'h6'), ('h7', 'h7')], required=False))])), ('paragraph', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(required=True))])), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alt_text', wagtail.core.blocks.TextBlock(required=True)), ('caption', wagtail.core.blocks.TextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))])), ('quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock(required=True)), ('attribution', wagtail.core.blocks.CharBlock(required=True)), ('citation_text', wagtail.core.blocks.CharBlock(required=False)), ('citation_link', wagtail.core.blocks.URLBlock(required=False))])), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='view', template='blocks/default_block.html'))], blank=True, verbose_name='Page content blocks.')),
                ('thank_you', wagtail.core.fields.RichTextField(blank=True, help_text='Content to display after form submission.')),
                ('image', models.ForeignKey(blank=True, help_text='Banner image for the page header.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('clean_name', models.CharField(blank=True, default='', help_text='Safe name of the form field, the label converted to ascii_snake_case', max_length=255, verbose_name='name')),
                ('label', models.CharField(help_text='The label of the form field', max_length=255, verbose_name='label')),
                ('field_type', models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('multiselect', 'Multiple select'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time'), ('hidden', 'Hidden field')], max_length=16, verbose_name='field type')),
                ('required', models.BooleanField(default=True, verbose_name='required')),
                ('choices', models.TextField(blank=True, help_text='Comma separated list of choices. Only applicable in checkboxes, radio and dropdown.', verbose_name='choices')),
                ('default_value', models.CharField(blank=True, help_text='Default value. Comma separated values supported for checkboxes.', max_length=255, verbose_name='default value')),
                ('help_text', models.CharField(blank=True, max_length=255, verbose_name='help text')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='core.formpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FlexPageGalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('caption', models.CharField(blank=True, max_length=250)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='core.flexpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]