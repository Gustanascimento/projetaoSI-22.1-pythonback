# Generated by Django 4.1.1 on 2022-10-11 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_imageurl_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageurl',
            name='url',
            field=models.URLField(blank=True, default='www.example.com', null=True),
        ),
    ]