# Generated by Django 3.0.2 on 2020-01-11 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_cartitem_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]