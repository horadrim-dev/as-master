# Generated by Django 4.2.9 on 2024-03-23 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0004_remove_price_placeholder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='price',
            old_name='text',
            new_name='description',
        ),
    ]
