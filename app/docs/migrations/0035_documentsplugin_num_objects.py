# Generated by Django 4.2.3 on 2023-09-07 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0034_remove_documentsplugin_tags_documentsplugin_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentsplugin',
            name='num_objects',
            field=models.PositiveIntegerField(default=8, verbose_name='Количество объектов'),
        ),
    ]
