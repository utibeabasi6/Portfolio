# Generated by Django 3.2.4 on 2021-06-11 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0007_services'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Services',
            new_name='Service',
        ),
    ]
