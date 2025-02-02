from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import *
from taggit.forms import TagField
from taggit_labels.widgets import LabelWidget
from django.urls import reverse_lazy
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import RegionalPhoneNumberWidget
from .models import ContactSettings
from filer.fields.file import FilerFileField
from django.core.validators import FileExtensionValidator
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox


class ContactForm(forms.Form):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # загружаем модель с настройками приложения
        self.settings = ContactSettings.load()

class AgreementForm(ContactForm):
    accept_terms = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={
            "class": "form-check-input"
        })
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.html_before_form = self.settings.agreement
        self.fields['accept_terms'].label = self.settings.agreement_checkbox_text

class UserDataForm(ContactForm):
    lastname = forms.CharField(label="Фамилия",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Укажите вашу фамилию"
        })
    )
    firstname = forms.CharField(label="Имя",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Укажите ваше имя"
        })
    )
    middlename = forms.CharField(label="Отчество",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Укажите ваше отчество"
        })
    )
    email = forms.EmailField(label="Электронная почта",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Укажите ваш адрес электронной почты"
        })
    )
    phone = PhoneNumberField(label="Телефон",
        widget=RegionalPhoneNumberWidget(attrs={
            "class": "form-control",
            "placeholder": "+7xxxxxxxxxx"
        })
    )

    agree_pd = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={
            "class": "form-check-input",
            "placeholder": "+7 1112223344"
        })
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.html_before_form = self.settings.userdata_form_text
        self.fields['agree_pd'].label = self.settings.userdata_checkbox_text

class MessageForm(ContactForm):
    # subject = forms.CharField(
    #     label="Тема обращения",
    #     widget=forms.TextInput(attrs={
    #         "class": "form-control",
    #         "placeholder": "Укажите суть обращения"
    #     })
    # )
    attachment_passport = forms.FileField(required=False, label="Паспорт (основная информация)",
                                   widget=forms.ClearableFileInput(attrs={"class": "form-control"}))
    attachment_snils = forms.FileField(required=False, label="СНИЛС",
                                   widget=forms.ClearableFileInput(attrs={"class": "form-control"}))
    attachment_photo = forms.FileField(required=False,  label="Фото 3х4",
                                   widget=forms.ClearableFileInput(attrs={"class": "form-control"}))
    attachment_spravka = forms.FileField(required=False, label="Водительская мед.справка",
                                   widget=forms.ClearableFileInput(attrs={"class": "form-control"}))
    # attachment_1 = forms.FileField(required=False, 
    #                                widget=forms.ClearableFileInput(attrs={"class": "form-control"}))
    # attachment_2 = forms.FileField(required=False, 
    #                                widget=forms.ClearableFileInput(attrs={"class": "form-control"}))
    # attachment_3 = forms.FileField(required=False, 
    #                                widget=forms.ClearableFileInput(attrs={"class": "form-control"}))
    message = forms.CharField(
        required=False,
        label="Комментарий",
        widget=forms.Textarea(attrs={
            "class": "form-control",
        })
    )

    # Капча отключена изза ошибки "timeout-or-duplicate"
    #captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.html_before_form = self.settings.message_form_text
        # загружаем разрешенные расширения файлов из настроек в валидатор
        validators_list = [FileExtensionValidator(self.settings.valid_extensions)]
        self.fields['attachment_passport'].validators = validators_list
        self.fields['attachment_snils'].validators = validators_list
        self.fields['attachment_photo'].validators = validators_list
        self.fields['attachment_spravka'].validators = validators_list
        # self.fields['attachment_1'].validators = validators_list
        # self.fields['attachment_2'].validators = validators_list
        # self.fields['attachment_3'].validators = validators_list