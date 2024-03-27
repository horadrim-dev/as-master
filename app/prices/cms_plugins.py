from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _
from django.contrib import admin

from .models import PricesPlugin


@plugin_pool.register_plugin
class PricesPluginPublisher(CMSPluginBase):
    model = PricesPlugin
    name = "Цены"
    render_template = "prices/prices.plugin.html"
    cache = True

    def render(self, context, instance, placeholder):
        context.update({
            # 'id': instance.generate_id(),
            'object_list': instance.get_prices(),
        })
        return context

