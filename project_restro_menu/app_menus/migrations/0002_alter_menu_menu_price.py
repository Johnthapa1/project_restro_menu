# Generated by Django 4.2.1 on 2023-06-14 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_menus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='menu_price',
            field=models.FloatField(default=0.0),
        ),
    ]
