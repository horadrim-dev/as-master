from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

@apphook_pool.register
class PricesApphook(CMSApp):
    app_name = "prices"  # must match the application namespace
    name = "Тарифы"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["prices.urls"] # replace this with the path to your application's URLs module