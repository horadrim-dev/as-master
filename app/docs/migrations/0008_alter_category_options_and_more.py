# Generated by Django 4.2.3 on 2023-08-11 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0007_rename_hide_document_type_documenttype_show_document_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['order'], 'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
        migrations.AlterField(
            model_name='documenttype',
            name='show_document_type',
            field=models.BooleanField(default=True, verbose_name='Отображать тип документа, номер и дату (если они заданы) в названии'),
        ),
    ]
