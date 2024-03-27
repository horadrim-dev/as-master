# Generated by Django 4.2.3 on 2023-10-03 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_event_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='button_text',
            field=models.CharField(default='Хорошо', max_length=64, verbose_name='Текст кнопки'),
        ),
        migrations.AddField(
            model_name='event',
            name='use_button',
            field=models.BooleanField(default=True, verbose_name='Использовать кнопку'),
        ),
    ]
