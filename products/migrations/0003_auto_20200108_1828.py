# Generated by Django 3.0.2 on 2020-01-08 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_kit_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='vipslot',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='kit',
            name='quantity',
            field=models.PositiveIntegerField(default=10),
        ),
    ]
