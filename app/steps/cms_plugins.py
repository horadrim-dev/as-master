from django.utils.translation import gettext_lazy as _

from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

# from .forms import *
from .models import *

@plugin_pool.register_plugin
class StepsPluginPublisher(CMSPluginBase):
    model = StepsPlugin
    module = "Контейнеры"
    name = "Шаги (этапы)"
    render_template = "steps/steps.html"
    allow_children = True
    child_classes = ["StepPluginPublisher"]
    # form = ColumnsForm

    # def save_model(self, request, obj, form, change):
    #     response = super().save_model(
    #         request, obj, form, change
    #     )
    #     child_objects = CMSPlugin.objects.filter(parent=obj, plugin_type=StepPluginPublisher.__name__)
    #     for idx, col in enumerate(form.cleaned_data['create'].split('-')):
    #         bootstrap_col = "col-md-{}".format(col)

    #         if len(child_objects) >= idx + 1:
    #             column_obj = Column.objects.get(id=child_objects[idx].id)
    #             column_obj.classes = bootstrap_col
    #             column_obj.save()
    #         else:
    #             col = Column(
    #                 parent=obj,
    #                 placeholder=obj.placeholder,
    #                 language=obj.language,
    #                 # width=form.cleaned_data['create_width'],
    #                 classes=bootstrap_col,
    #                 position=CMSPlugin.objects.filter(parent=obj).count(),
    #                 plugin_type=ColumnPlugin.__name__
    #             )
    #             col.save()
    #     return response


@plugin_pool.register_plugin
class StepPluginPublisher(CMSPluginBase):
    model = StepPlugin
    # module = "Шаги (этапы)"
    name = "Шаг"
    render_template = "steps/step.html"
    parent_classes = ["StepsPluginPublisher"]
    allow_children = True


