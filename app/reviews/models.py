from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _
from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField
from filer.models.imagemodels import Image
import uuid


class ReviewsPlugin(CMSPlugin):


    def get_reviews(self):
        return Review.objects.filter(published=True)[:20]

    def generate_id(self):
        return str(uuid.uuid4().fields[-1])[:7]

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

class Review(models.Model):
    # plugin = models.ForeignKey(
    #         Reviews,
    #         on_delete=models.CASCADE,
    #     )
    published = models.BooleanField("Опубликовано", default=False)
    author = models.CharField("Автор", max_length=255, default="")
    text = models.TextField("Содержимое", default="")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    # photo = FilerImageField(
    #     verbose_name=_('Фото автора'),
    #     on_delete=models.CASCADE, 
    #     help_text="Не обязательно для заполнения.",
    #     blank=True, null=True
    # )

    def __str__(self):
        return self.author

    class Meta:
        ordering = ['-created_at']
        verbose_name = "отзыв"
        verbose_name_plural = "отзывы"
