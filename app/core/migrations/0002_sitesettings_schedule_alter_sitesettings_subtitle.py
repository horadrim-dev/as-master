# Generated by Django 4.2.9 on 2024-02-07 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='schedule',
            field=models.CharField(default='', max_length=256, verbose_name='График работы'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='subtitle',
            field=models.CharField(blank=True, default='', max_length=256, null=True, verbose_name='Подзаголовок'),
        ),
    ]
