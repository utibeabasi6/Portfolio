# Generated by Django 3.2.4 on 2021-06-12 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0009_service_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]