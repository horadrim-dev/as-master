# Generated by Django 4.1.7 on 2023-02-27 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_sitesettings_address_alter_sitesettings_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sitesettings',
            options={'verbose_name': 'Конфигурация сайта', 'verbose_name_plural': 'Конфигурация сайта'},
        ),
    ]
