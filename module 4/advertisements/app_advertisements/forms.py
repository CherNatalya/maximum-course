from django import forms
from .models import Advertisement
from django.core.exceptions import ValidationError


def validate_title(value):
    if not value.lower().isalpha():
        raise ValidationError('Заголовок должен состоять только из буквенных символов')


class AdvertisementForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AdvertisementForm, self).__init__(*args, **kwargs)
        self.fields['title'].validators = [validate_title]

    class Meta:
        model = Advertisement
        exclude = ['created_at', 'updated_at', 'user']
        widgets = {'title_new': [forms.TextInput(attrs={'class': 'form-control form-control-lg'})],
                   'description': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
                   'price': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
                   'auction': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                   'image': forms.FileInput(attrs={'class': 'form-control form-control-lg'})}
