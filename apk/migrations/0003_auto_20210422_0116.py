# Generated by Django 3.2 on 2021-04-21 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apk', '0002_auto_20210422_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='order/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product/'),
        ),
    ]
