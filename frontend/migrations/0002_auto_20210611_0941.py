# Generated by Django 3.2.4 on 2021-06-11 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('proficiency', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='work',
            name='category',
            field=models.CharField(choices=[('web', 'Web'), ('mobile', 'Mobile'), ('design', 'Design')], default='Web', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='description',
            field=models.TextField(default='A project'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]
