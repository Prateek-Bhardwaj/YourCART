# Generated by Django 3.2 on 2021-04-30 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apk', '0017_delete_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending', max_length=198),
        ),
    ]
