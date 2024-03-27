# Generated by Django 4.2.3 on 2023-09-20 06:39

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('events', '0003_remove_event_finish_at_alter_event_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='poster',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.FILER_IMAGE_MODEL, verbose_name='Обложка'),
        ),
    ]
