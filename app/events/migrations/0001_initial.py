# Generated by Django 4.2.9 on 2024-02-04 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import djangocms_text_ckeditor.fields
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'категория мероприятий',
                'verbose_name_plural': 'категории мероприятий',
            },
        ),
        migrations.CreateModel(
            name='UpcomingEventsPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.cmsplugin')),
                ('num_objects', models.PositiveIntegerField(default=3, verbose_name='Количество мероприятий')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.categoryevent', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='Название мероприятия')),
                ('description', djangocms_text_ckeditor.fields.HTMLField(blank=True, null=True, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Последнее изменение')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.categoryevent', verbose_name='Категория')),
                ('poster', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.FILER_IMAGE_MODEL, verbose_name='Обложка')),
            ],
            options={
                'verbose_name': 'мероприятие',
                'verbose_name_plural': 'мероприятия',
            },
        ),
        migrations.CreateModel(
            name='DayEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время начала мероприятия')),
                ('place', models.CharField(blank=True, max_length=256, null=True, verbose_name='Место проведения')),
                ('postfix_name', models.CharField(blank=True, help_text='Пример: День 1, Второй этап и т.д.                                                Будет отображено в квадратных скобках в                                                конце названия мероприятия.', max_length=1024, null=True, verbose_name='Постфикс названия мероприятия')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Последнее изменение')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
            options={
                'verbose_name': 'день',
                'verbose_name_plural': 'дни мероприятия',
                'ordering': ['start_at'],
            },
        ),
        migrations.CreateModel(
            name='CalendarEventsPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.cmsplugin')),
                ('category', models.ForeignKey(blank=True, help_text='Оставьте пустым для использования всех категорий', null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.categoryevent', verbose_name='Категория мероприятий')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
