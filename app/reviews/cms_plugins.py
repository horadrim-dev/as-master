from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _
from django.contrib import admin

from .models import ReviewsPlugin


@plugin_pool.register_plugin
class ReviewsPluginPublisher(CMSPluginBase):
    model = ReviewsPlugin
    name = "Отзывы"
    render_template = "reviews.html"
    cache = True

    def render(self, context, instance, placeholder):
        context.update({
            'id': instance.generate_id(),
            'reviews': instance.get_reviews(),
        })
        return context

