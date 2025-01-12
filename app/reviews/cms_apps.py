from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

@apphook_pool.register
class ReviewsApphook(CMSApp):
    app_name = "reviews"  # must match the application namespace
    name = "Отзывы"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["reviews.urls"] # replace this with the path to your application's URLs module