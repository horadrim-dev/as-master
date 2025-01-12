from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar
from cms.cms_toolbars import PAGE_MENU_IDENTIFIER
from cms.extensions.toolbar import ExtensionToolbar
from cms.utils.urlutils import admin_reverse
from django.urls import reverse 
from .models import Review

@toolbar_pool.register
class ReviewsToolbar(CMSToolbar):

    # we are getting redirect to model.get_absolute_url instance after save
    watch_models = [Review]

    def populate(self):


        # self.toolbar.add_sideframe_button(
        #     name='Новости', 
        #     url=admin_reverse('reviews_post_changelist'),
        #     )

        page_menu = self.toolbar.get_menu(PAGE_MENU_IDENTIFIER)

        reviews_menu = self.toolbar.get_or_create_menu(
            key='reviews_cms_integration',
            verbose_name='Отзывы',
            position = page_menu
        )
        reviews_menu .add_sideframe_item(
            name='Отзывы',
            url=admin_reverse('reviews_review_changelist')
        )
