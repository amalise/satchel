# Generated by Django 4.0.3 on 2022-04-05 06:42

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('wagtailimages', '0023_add_choose_permissions'),
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('project_title', models.CharField(max_length=150)),
                ('date', models.DateField(verbose_name='Article Date')),
                ('intro', models.TextField()),
                ('image', models.ForeignKey(help_text='Project Image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('testimonials', models.ForeignKey(blank=True, help_text='Project Testimonials', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='snippets.testimonial')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PortfolioPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('headline_text', models.CharField(blank=True, help_text='Blog listing page header text.', max_length=70)),
                ('experience', wagtail.core.fields.StreamField([('timeline_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=100)), ('text', wagtail.core.blocks.TextBlock()), ('date', wagtail.core.blocks.DateBlock())]))], blank=True, null=True)),
                ('background_image', models.ForeignKey(help_text='Header background image.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
