# Generated by Django 4.2.9 on 2024-04-01 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_animated_numbers', '0008_remove_animatednumbers_image_number_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='number',
            name='image',
        ),
    ]
