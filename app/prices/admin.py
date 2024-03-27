from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from .models import Price


@admin.register(Price)
class PriceAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    # поле alias будет автоматически заполнено на основе заголовка
    # prepopulated_fields = {
    #     "alias" : ("title",)
    model = Price
    # form = ReviewForm