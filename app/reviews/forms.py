from django import forms
from .models import Review
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields = []
        exclude = []

class LeaveReviewForm(forms.Form):
    author = forms.CharField(label="Имя",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Как вас зовут?"
        })
    )
    text = forms.CharField(label="Текст",
        widget=forms.Textarea(attrs={"rows":"5", 
                                     "class":"form-control",
                                     "placeholder":"Поделитесь впечатлениями"})
        )

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.html_before_form = self.settings.userdata_form_text
    #     self.fields['agree_pd'].label = self.settings.userdata_checkbox_text