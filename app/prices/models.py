from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField
from djangocms_text_ckeditor.fields import HTMLField
from easy_thumbnails.files import get_thumbnailer
from cms.models.fields import PageField, PlaceholderField 
import uuid


class PricesPlugin(CMSPlugin):


    def get_prices(self):
        return Price.objects.all()

    # def generate_id(self):
    #     return str(uuid.uuid4().fields[-1])[:7]

    # def copy_relations(self, oldinstance):
    #     # Before copying related objects from the old instance, the ones
    #     # on the current one need to be deleted. Otherwise, duplicates may
    #     # appear on the public version of the page
    #     self.revi_set.all().delete()

    #     for slide in oldinstance.slide_set.all():
    #         # instance.pk = None; instance.pk.save() is the slightly odd but
    #         # standard Django way of copying a saved model instance
    #         slide.pk = None
    #         slide.slider = self
    #         slide.save()

class Price(models.Model):

    # page = PageField(verbose_name="Страница с подробной информацией")
    placeholder = PlaceholderField(slotname="content")
    title = models.CharField("Название", max_length=1024, default="")
    subtitle = models.CharField("Подзаголовок", max_length=512, default="")
    value  = models.CharField("Стоимость", max_length=64, default="")
    description = HTMLField("Описание", default="")
    image = FilerImageField(
        verbose_name=_('Картинка'),
        on_delete=models.CASCADE, 
        blank=True, null=True
    )

    def __str__(self):
        return self.title

    def thumb_src(self):
        image = self.image
        if not image:
            return None

        thumbnail_options = {
            'size': (360, 240),
            'crop': True,
            'upscale': True,
            'autocrop': False,
            'subject_location': image.subject_location,
        }
        thumbnailer = get_thumbnailer(image)
        return thumbnailer.get_thumbnail(thumbnail_options).url

    def get_absolute_url(self):
        return reverse('prices:detail', kwargs={'pk': self.pk})


    class Meta:
        verbose_name = "тариф"
        verbose_name_plural = "тарифы"
