# Generated by Django 4.2.9 on 2024-03-29 04:49

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('djangocms_animated_numbers', '0006_alter_animatednumbers_cmsplugin_ptr'),
    ]

    operations = [
        migrations.AddField(
            model_name='animatednumbers',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.FILER_IMAGE_MODEL, verbose_name='Картинка'),
        ),
    ]
