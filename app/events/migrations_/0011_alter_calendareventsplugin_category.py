# Generated by Django 4.2.3 on 2023-10-06 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_calendareventsplugin_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendareventsplugin',
            name='category',
            field=models.ForeignKey(blank=True, help_text='Оставьте пустым для использования всех категорий', null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.categoryevent', verbose_name='Категория мероприятий'),
        ),
    ]
