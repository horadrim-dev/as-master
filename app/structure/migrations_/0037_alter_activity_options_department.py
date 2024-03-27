# Generated by Django 4.2.3 on 2023-09-13 03:25

from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0036_activity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name': 'вид деятельности', 'verbose_name_plural': 'виды деятельности'},
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField(blank=True, default=0, help_text='Если оставить равным 0 - добавится в конец.', null=True, verbose_name='Порядок')),
                ('name', models.CharField(verbose_name='Название')),
                ('description', djangocms_text_ckeditor.fields.HTMLField(verbose_name='Описание')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.activity', verbose_name='Вид деятельности')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.organization', verbose_name='Организация')),
            ],
            options={
                'verbose_name': 'секция',
                'verbose_name_plural': 'секции',
            },
        ),
    ]
