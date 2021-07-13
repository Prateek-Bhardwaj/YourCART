# Generated by Django 3.2 on 2021-04-27 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apk', '0012_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(blank=True, max_length=198, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('quantity', models.IntegerField(default=1)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='apk.product')),
            ],
        ),
    ]
