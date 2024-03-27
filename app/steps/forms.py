from django import forms

from .models import StepsPlugin


class StepsPluginForm(forms.ModelForm):

    # create = forms.ChoiceField(
    #     choices=NUM_COLUMNS,
    #     label="Кол-во шагов",
    #     # help_text=_("Create this number of columns")
    # )
    # num_steps = forms.
    # create_width = forms.ChoiceField(
    #     choices=WIDTH_CHOICES,
    #     label=_("Column width"),
    #     help_text=_(
    #         "Width of created columns. You can still change the width of the "
    #         "column afterwards."
    #     )
    # )

    class Meta:
        model = StepsPlugin
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')
