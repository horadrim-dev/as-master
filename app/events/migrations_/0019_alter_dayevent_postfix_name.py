# Generated by Django 4.2.3 on 2023-10-09 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0018_alter_dayevent_postfix_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayevent',
            name='postfix_name',
            field=models.CharField(blank=True, help_text='Пример: День 1, Второй этап и т.д.                                                Будет отображено в квадратных скобках в                                                конце названия мероприятия.', null=True, verbose_name='Постфикс названия мероприятия'),
        ),
    ]
