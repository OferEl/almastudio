# Generated by Django 3.0.5 on 2020-04-17 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('email_id', models.AutoField(primary_key=True, serialize=False)),
                ('email_name', models.CharField(max_length=50)),
                ('email_email', models.CharField(max_length=50)),
                ('email_phone', models.CharField(max_length=50)),
                ('email_text', models.TextField(default='none')),
                ('email_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
