# Generated by Django 4.1.7 on 2023-06-22 10:27

import cms.models.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djangocms_attributes_field.fields
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('filer', '0015_alter_file_owner_alter_file_polymorphic_ctype_and_more'),
        ('cms', '0022_auto_20180620_1551'),
        ('medialer', '0007_rename_picture_pluginpicture'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template', models.CharField(choices=[('default', 'Default')], default='default', max_length=255, verbose_name='Template')),
                ('external_picture', models.URLField(blank=True, help_text='If provided, overrides the embedded image. Certain options such as cropping are not applicable to external images.', max_length=255, null=True, verbose_name='External image')),
                ('width', models.PositiveIntegerField(blank=True, help_text='The image width as number in pixels. Example: "720" and not "720px".', null=True, verbose_name='Width')),
                ('height', models.PositiveIntegerField(blank=True, help_text='The image height as number in pixels. Example: "720" and not "720px".', null=True, verbose_name='Height')),
                ('alignment', models.CharField(blank=True, choices=[('left', 'Align left'), ('right', 'Align right'), ('center', 'Align center')], help_text='Aligns the image according to the selected option.', max_length=255, verbose_name='Alignment')),
                ('caption_text', models.TextField(blank=True, help_text='Provide a description, attribution, copyright or other information.', null=True, verbose_name='Caption text')),
                ('attributes', djangocms_attributes_field.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
                ('link_url', models.URLField(blank=True, help_text='Wraps the image in a link to an external URL.', max_length=2040, null=True, verbose_name='External URL')),
                ('link_target', models.CharField(blank=True, choices=[('_blank', 'Open in new window'), ('_self', 'Open in same window'), ('_parent', 'Delegate to parent'), ('_top', 'Delegate to top')], max_length=255, verbose_name='Link target')),
                ('link_attributes', djangocms_attributes_field.fields.AttributesField(blank=True, default=dict, verbose_name='Link attributes')),
                ('use_automatic_scaling', models.BooleanField(blank=True, default=True, help_text='Uses the placeholder dimensions to automatically calculate the size.', verbose_name='Automatic scaling')),
                ('use_no_cropping', models.BooleanField(blank=True, default=False, help_text='Outputs the raw image without cropping.', verbose_name='Use original image')),
                ('use_crop', models.BooleanField(blank=True, default=False, help_text='Crops the image according to the thumbnail settings provided in the template.', verbose_name='Crop image')),
                ('use_upscale', models.BooleanField(blank=True, default=False, help_text='Upscales the image to the size of the thumbnail settings in the template.', verbose_name='Upscale image')),
                ('use_responsive_image', models.CharField(choices=[('inherit', 'Let settings.DJANGOCMS_PICTURE_RESPONSIVE_IMAGES decide'), ('yes', 'Yes'), ('no', 'No')], default='inherit', help_text='Uses responsive image technique to choose better image to display based upon screen viewport. This configuration only applies to uploaded images (external pictures will not be affected). ', max_length=7, verbose_name='Use responsive image')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medialer.album', verbose_name='Альбом')),
                ('link_page', cms.models.fields.PageField(blank=True, help_text='Wraps the image in a link to an internal (page) URL.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.page', verbose_name='Internal URL')),
                ('picture', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.FILER_IMAGE_MODEL, verbose_name='Image')),
                ('thumbnail_options', models.ForeignKey(blank=True, help_text='Overrides width, height, and crop; scales up to the provided preset dimensions.', null=True, on_delete=django.db.models.deletion.CASCADE, to='filer.thumbnailoption', verbose_name='Thumbnail options')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
