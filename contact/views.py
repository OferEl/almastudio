from django.shortcuts import render
from django.views.generic import FormView
from .forms import Contact
from django.core.mail import send_mail
from django.utils.decorators import method_decorator


# Create your views here.

class Contactus(FormView):
    template_name = 'contactus.html'
    form_class = Contact
    success_url = '/contactus/'


    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def sendmail(self,name, to, phone, text):
        message = 'אנו ניצור קשר בהקדם , תודה צוות django-lab.' + '   הפרטים המצורפים ' +phone + '  -  '+ text
        send_mail(
            ['תודה שפנית אלינו'],
            message,
            'oferel@zohomail.com',
            [to , 'oferel1@gmail.com'],
            fail_silently=False,
        )

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():

            name = form.cleaned_data['email_name']
            to = form.cleaned_data['email_email']
            phone = form.cleaned_data['email_phone']
            text = form.cleaned_data['email_text']
            self.sendmail(name, to, phone, text)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

