# Generated by Django 3.2.4 on 2021-06-11 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0008_rename_services_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='description',
            field=models.TextField(default='Basically means that I make websites'),
            preserve_default=False,
        ),
    ]
