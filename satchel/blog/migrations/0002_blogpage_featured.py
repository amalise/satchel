# Generated by Django 4.0.3 on 2022-04-04 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
