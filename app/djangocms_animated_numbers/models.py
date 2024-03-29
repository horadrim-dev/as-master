from email.policy import default
from django.db import models
from django.utils.translation import gettext_lazy as _
from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField
from easy_thumbnails.files import get_thumbnailer
import uuid


class AnimatedNumbers(CMSPlugin):

    duration = models.PositiveIntegerField("Время действия анимации (миллисекунды, 1сек=1000мс)", default=5000)

    def get_numbers(self):
        return self.number_set.all()

    def generate_id(self):
        return str(uuid.uuid4().fields[-1])[:7]

    def copy_relations(self, oldinstance):
        # Before copying related objects from the old instance, the ones
        # on the current one need to be deleted. Otherwise, duplicates may
        # appear on the public version of the page
        self.number_set.all().delete()

        for slide in oldinstance.number_set.all():
            # instance.pk = None; instance.pk.save() is the slightly odd but
            # standard Django way of copying a saved model instance
            slide.pk = None
            slide.plugin = self
            slide.save()

class Number(models.Model):
    plugin = models.ForeignKey(
            AnimatedNumbers,
            on_delete=models.CASCADE,
        )
    number = models.IntegerField("Значение показателя", default=999)
    title = models.CharField("Подпись", max_length=256,  default="")
    # image = FilerImageField(verbose_name="Картинка", on_delete=models.CASCADE,
    #                         blank=True, null=True, help_text="120x120")

    def __str__(self):
        return '{} {}'.format(self.number, self.title)

    # def thumb_src(self):
    #     image = self.image

    #     thumbnail_options = {
    #         'size': (120, 120),
    #         'crop': True,
    #         'upscale': True,
    #         'autocrop': False,
    #         'subject_location': image.subject_location,
    #     }
    #     thumbnailer = get_thumbnailer(image)

    class Meta:
        verbose_name = "анимированный показатель"
        verbose_name_plural = "анимированные показатели"
