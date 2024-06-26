# Generated by Django 4.2.3 on 2023-09-01 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_whitespaceplugin_remove_headerplugin_size_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='headerplugin',
            name='align',
            field=models.CharField(choices=[('left', 'Слева'), ('center', 'По центру'), ('right', 'Справа')], default='left', verbose_name='Выравнивание'),
        ),
        migrations.AddField(
            model_name='headerplugin',
            name='layout',
            field=models.CharField(choices=[('bold-line', 'С жирной линией'), ('thin-line', 'С тонкой линией'), ('no-line', 'Без линии')], default='bold-line', verbose_name='Размер'),
        ),
    ]
