# Generated by Django 3.2.4 on 2021-06-19 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0011_interest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='services',
        ),
    ]
