# Generated by Django 4.2.6 on 2023-10-19 06:23

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('infoblock', '0007_delete_slide'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.cmsplugin')),
                ('background_color', colorfield.fields.ColorField(blank=True, default='#FFFFFF', image_field=None, max_length=18, null=True, samples=None, verbose_name='Цвет фона')),
                ('container_type', models.CharField(choices=[('container', 'С отступами справа и слева'), ('container-fluid no-paddings', 'Во всю ширину')], default='container', max_length=64, verbose_name='Расположение контента')),
            ],
            options={
                'verbose_name': 'слайд',
                'verbose_name_plural': 'слайды',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
