# Generated by Django 4.1.7 on 2023-06-08 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breadcrumbs', '0002_remove_breadcrumbs_thumb_height_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='breadcrumbs',
            name='shadow',
            field=models.BooleanField(default=False, verbose_name='Тень для текста'),
        ),
    ]
