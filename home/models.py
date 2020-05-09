from django.db import models

class Email (models.Model):

    email_id = models.AutoField(primary_key=True)
    email_name = models.CharField(max_length=50,blank=True)
    email_email = models.CharField(max_length=50)
    email_phone = models.CharField(max_length=50,blank=True)
    email_text = models.TextField(default='none',blank=True)
    email_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.email_id