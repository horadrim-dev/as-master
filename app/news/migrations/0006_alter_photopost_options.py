# Generated by Django 4.2.9 on 2024-02-13 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_photopost'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photopost',
            options={'ordering': ['-created_at'], 'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
    ]
