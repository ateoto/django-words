from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django_summernote.widgets import SummernoteInplaceWidget

from words.models import Entry


class EntryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EntryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('submit', 'Submit'))

    class Meta:
        model = Entry
        fields = '__all__'
        widgets = {
        	'text': SummernoteInplaceWidget(),
        }
