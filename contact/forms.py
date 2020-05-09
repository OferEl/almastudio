from django import forms
from home.models import Email

class Email(forms.ModelForm):

    class Meta:
        model = Email
        fields = ['email_name', 'email_email','email_phone' ,'email_text' ]

    def clean_email_name(self):
        data = self.cleaned_data['first_name']
        if data == 'ofer':
            raise forms.ValidationError("You must select name image!")
        return data

    def clean_email_email(self):
        data = self.cleaned_data['email_email']
        return data


from django import forms

class Contact(forms.Form):
    email_name = forms.CharField(max_length=100)
    email_phone = forms.CharField(max_length=100)
    email_text = forms.CharField(widget=forms.Textarea)
    email_email = forms.EmailField()