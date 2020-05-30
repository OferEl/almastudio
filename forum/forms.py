from django.forms import ModelForm , forms
from .models import Forum

class Newtopic(ModelForm):
    class Meta:
        model = Forum
        fields = [ 'forum_title', 'forum_text']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("forum_title")
        text = cleaned_data.get("forum_text")
