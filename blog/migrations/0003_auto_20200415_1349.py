# Generated by Django 3.0.5 on 2020-04-15 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200415_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='blog_desc1',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='blog_desc2',
        ),
    ]
