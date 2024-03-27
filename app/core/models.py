from django.db import models, transaction
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField
from cms.models.pagemodel import Page
from cms.models.pluginmodel import CMSPlugin

class OrderedModel(models.Model):
    
    order = models.PositiveSmallIntegerField(default=0, blank=True, null=True, verbose_name="Порядок", help_text="Если оставить равным 0 - добавится в конец.")

    def update_order(self, list_of_objects):
            '''обновляет порядок элементов с общим родителем'''
            # получаем соседние объекты
            objects = list_of_objects
            objects_count = len(objects)
            # формируем список новых ордеров
            orders = [i for i in range(1, objects_count + 1 + 1)]

            # если новый ордер за пределами возможных или равен 0
            if (self.order > objects_count + 1) or (self.order <= 0):

                with transaction.atomic():
                    # просто присваем последний ордер
                    self.order = orders[-1]
                    self.save(update_fields=['order'], lock_recursion=True)
                    # обновляем соседние меню
                    for i in orders[:-1]:
                        objects[i-1].order = i
                        objects[i-1].save(update_fields=['order'], lock_recursion=True)
                    
            else: # если новый ордер в пределах возможных
                # резервируем нужный ордер для изменяемого меню, другие меню расставляем по остальным ордерам
                obj_num = 0
                with transaction.atomic():
                    for i in orders:
                        if i != self.order:
                            objects[obj_num].order = i
                            objects[obj_num].save(update_fields=['order'], lock_recursion=True)
                            obj_num += 1

    class Meta:
        abstract = True
        ordering = ['order']


class MenuItemSettingsExtension(PageExtension):
    ''' 
    Adding text font-awesome name icon to page 
    for displaying in menu 
    '''
    fa_icon = models.CharField(verbose_name="Иконка пункта меню",
                                help_text='Названия иконок брать <a href="https://fontawesome.com/v4/icons/" target="blank">отсюда</a>', 
                                max_length=32, default="", 
                                blank=True, )
    dropdown_mega = models.BooleanField(verbose_name="Mega Dropdown", default=False,
                                        help_text="Если отмечено, выпадающее меню будет во всю ширину \
                                        (работает только на верхнем уровне)")

extension_pool.register(MenuItemSettingsExtension)


class SingletonModel(models.Model):
    """Singleton Django Model
    https://gist.github.com/senko/5028413

    Ensures there's always only one entry in the database, and can fix the
    table (by deleting extra entries) even if added via another mechanism.
    Also has a static load() method which always returns the object - from
    the database if possible, or a new empty (default) instance if the
    database is still empty. If your instance has sane defaults (recommended),
    you can use it immediately without worrying if it was saved to the
    database or not.
    Useful for things like system-wide user-editable settings.
    """

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        Save object to the database. Removes all other entries if there
        are any.
        """
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        """
        Load object from the database. Failing that, create a new empty
        (default) instance of the object and return it (without saving it
        to the database).
        """

        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()

MENU_STYLE_CHOICES = [
    ("1", "Стиль №1"),
    ("2", "Стиль №2"),
]
class SiteSettings(SingletonModel):
    # site_url = models.URLField(verbose_name=_('Website url'), max_length=256)
    title = models.CharField(verbose_name=_('Заголовок'), max_length=256, default="")
    subtitle = models.CharField(verbose_name=_('Подзаголовок'), max_length=256, default="",
                                blank=True, null=True)
    phone = models.CharField(verbose_name=_('Телефон'), max_length=256, default="")
    email = models.EmailField(verbose_name='E-mail', blank=True, null=True)
    address = models.CharField(verbose_name=_('Адрес'), max_length=256, default="")
    schedule = models.CharField(verbose_name=_('График работы'), max_length=256, default="")
    share_vk = models.BooleanField(verbose_name="Share Вконтакте", default=True)
    share_ok = models.BooleanField(verbose_name="Share Одноклассники", default=True)
    share_fb = models.BooleanField(verbose_name="Share Facebook", default=False)
    share_twitter = models.BooleanField(verbose_name="Share Twitter", default=False)
    # menu_style = models.CharField(max_length=10, verbose_name="Макет главного меню",
    #                               choices=MENU_STYLE_CHOICES, default=MENU_STYLE_CHOICES[0][0])

    logo = FilerImageField(
        verbose_name=_('Логотип'),
        on_delete=models.CASCADE,
        blank=True, null=True
    )
 
    def __str__(self):
        return 'Конфигурация сайта'

    def socials(self):
        return self.social_set.all()

    class Meta:
        verbose_name = "Конфигурация сайта"
        verbose_name_plural = "Конфигурация сайта"

class Social(models.Model):
    sitesettings = models.ForeignKey(SiteSettings, on_delete=models.CASCADE,)
    text = models.CharField(verbose_name='Текст', help_text="Примеры: \"ВК\", \"Мы в контакте\", \"Мы в ВК\"", max_length=256, default="")
    url = models.URLField(verbose_name="Ссылка на страницу в соц.сети.")
    icon = models.CharField(verbose_name="Иконка соц.сети",
                                help_text='Названия иконок брать <a href="https://fontawesome.com/v4/icons/" target="blank">отсюда</a>', 
                                max_length=32, default="")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "соц.сеть"
        verbose_name_plural = "соц.сети"


# class ExtendedPage(models.Model):   
#     # https://stackoverflow.com/questions/10293641/how-to-add-some-extra-fields-to-the-page-in-django-cms-in-django-admin-panel
#     page = models.OneToOneField(Page, unique=True, verbose_name=_("Page"), editable=False, related_name='extended_fields',
#                              on_delete=models.CASCADE)
#     test_field = models.CharField("TEST_FIELD", blank=True, null=True)

HEADER_LAYOUT_CHOICES = [
    ('bold-line', 'С жирной линией'),
    ('thin-line', 'С тонкой линией'),
    ('no-line', 'Без линии'),
]
HEADER_ALIGN_CHOICES = [
    ('left', 'Слева'),
    ('center', 'По центру'),
    ('right', 'Справа'),
]
SUBTITLE_POSITION_CHOICES = [
    ('bottom', 'Под заголовком'),
    ('top', 'Над заголовком'),
]
class HeaderPlugin(CMSPlugin):
    """Модель плагина выводящего заголовок"""
    title = models.CharField("Заголовок", max_length=1024, default=" ")
    subtitle = models.CharField("Подзаголовок (не обязательно)", max_length=1024, 
                                blank=True, null=True)
    layout = models.CharField("Стиль", max_length=32, choices=HEADER_LAYOUT_CHOICES, 
                              default=HEADER_LAYOUT_CHOICES[0][0])
    align = models.CharField("Выравнивание", max_length=32, choices=HEADER_ALIGN_CHOICES, 
                             default=HEADER_ALIGN_CHOICES[0][0])
    subtitle_position = models.CharField("Позиция подзаголовка", max_length=32, 
                                         choices=SUBTITLE_POSITION_CHOICES , 
                                         default=SUBTITLE_POSITION_CHOICES[0][0])

    def __str__(self):
        return self.title


WHITESPACE_CHOICES = [
    ('medium', 'Средне'),
    ('small', 'Чуть чуть'),
    ('large', 'Побольше'),
]
class WhitespacePlugin(CMSPlugin):
    """Модель плагина выводящего просто пустое место"""
    size = models.CharField("Размер", max_length=32, choices=WHITESPACE_CHOICES, default=WHITESPACE_CHOICES[0][0])


SUBMENU_LAYOUT_CHOICES = [
    ("blocks", "Блоки"),
    ("list", "Список")
]
class SubmenuPlugin(CMSPlugin):
    """Модель плагина выводящего дочернее меню"""
    layout = models.CharField("Макет", max_length=32, choices=SUBMENU_LAYOUT_CHOICES, default=SUBMENU_LAYOUT_CHOICES[0][0])
    parent_page = models.CharField("ID родителя (не обязательно)", max_length=32, blank=True, null=True,
                               help_text="Указывается идентификатор страницы, дочернее меню которой будет отображено. \
                                (ID заполняется в расширенных настройках страницы). Если не указано, будет отображено \
                                дочернее меню текущей страницы")
    

class PureCodePlugin(CMSPlugin):
    """Модель плагина позволяющего ввети пользовательский код"""
    # css = models.Text
    code = models.TextField("HTML", blank=True, null=True,
                            help_text="Использовать js и css здесь возможно, но не рекомендуется.")
    css = models.TextField("CSS", blank=True, null=True,)
    js = models.TextField("JAVASCRIPT", blank=True, null=True,
                          help_text="Доступно использование jQuery, пример \"$(document).ready(function () { \
                          alert(\"test\");});\"")


# TABS_POSITION_CHOICES = [
#     ("top", "Сверху"),
#     ("left", "Слева"),
#     ("right", "Справа"),
#     ("bottom", "Снизу"),
# ]
class TabsPlugin(CMSPlugin):
    """Модель плагина вкладок"""
    # tabs_position = models.CharField("Расположение переключателей вкладок", max_length=32, 
    #                                  choices=TABS_POSITION_CHOICES, default=TABS_POSITION_CHOICES[0][0])
    justified = models.BooleanField("Растянуть строку переключателей вкладок во всю ширину", default=True)
    num_auto_open = models.PositiveSmallIntegerField("Номер открытой вкладки", default=1,
                                                     help_text="если 0 - все вкладки будут закрыты")

class TabPlugin(CMSPlugin):
    """Модель плагина вкладки"""
    name = models.CharField("Название", max_length=128, )

    def __str__(self):
        return self.name

class AccordionPlugin(CMSPlugin):
    """Модель плагина аккордеон"""
    # speed = models.PositiveSmallIntegerField("Скорость раскрытия (мс)", default=1000)
    close_others = models.BooleanField("Клик по элементу будет закрывать другие вкладки", default=True)
    num_auto_open = models.PositiveSmallIntegerField("Номер открытой вкладки", default=1,
                                                     help_text="если 0 - все вкладки будут закрыты")
    open_all = models.BooleanField("Все вкладки развернуты при загрузке", default=False,
                                   help_text="Если активно, номер открытой вкладки будет проигнорирован")
    hide_borders = models.BooleanField("Скрыть линии границ аккордеона", default=False)

class ItemAccordionPlugin(CMSPlugin):
    """Модель плагина вкладки аккордеона"""
    name = models.CharField("Название", max_length=128, )

    def __str__(self):
        return self.name


class ItemArticlePlugin(CMSPlugin):
    """Модель плагина раздела статьи"""
    name = models.CharField("Название", max_length=128, )

    def __str__(self):
        return self.name