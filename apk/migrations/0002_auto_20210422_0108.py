# Generated by Django 3.2 on 2021-04-21 19:38

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
    ]
