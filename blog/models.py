# Create your models here.
from django.db import models

class Blog (models.Model):

    BLOG_TYPE = (
        ('Y', 'SHOW'),
        ('N', 'NO SHOW'),
    )

    blog_id = models.AutoField(primary_key=True)
    blog_type = models.CharField(max_length=1, choices=BLOG_TYPE)
    blog_title = models.CharField(max_length=50)
    blog_desc = models.CharField(max_length=1000)
    blog_text = models.TextField(default='none')
    blog_date = models.DateField(auto_now_add=True)
    blog_order = models.IntegerField(default=1)

    def __unicode__(self):
        return self.post_id