from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from cms.models import CMSPlugin

# if hasattr(settings, "COLUMN_WIDTH_CHOICES"):
#     WIDTH_CHOICES = settings.COLUMN_WIDTH_CHOICES
# else:
#     WIDTH_CHOICES = (
#         ('10%', _("10%")),
#         ('25%', _("25%")),
#         ('33.33%', _('33%')),
#         ('50%', _("50%")),
#         ('66.66%', _('66%')),
#         ('75%', _("75%")),
#         ('100%', _('100%')),
#     )


class StepsPlugin(CMSPlugin):
    """
    Плагин декоративной визуализации этапов(шагов)
    """
    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
        on_delete=models.CASCADE,
    )


    def __str__(self):
        plugins = self.child_plugin_instances or []
        return _("%s steps") % len(plugins)


class StepPlugin(CMSPlugin):
    """
    Модель плагина "Шаг" для StepsPlugin
    """
    # width = models.CharField(
    #     _("width"),
    #     choices=WIDTH_CHOICES,
    #     default=WIDTH_CHOICES[0][0],
    #     max_length=50
    # )

    classes = models.CharField("CSS классы", max_length=1000, default="", blank=True, null=True)

    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
        on_delete=models.CASCADE,
    )

    # def __str__(self):
    #     return "%s" % self.get_width_display()
