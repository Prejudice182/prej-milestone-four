# Generated by Django 3.0.2 on 2020-01-08 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200108_1828'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=300)),
                ('primaryCategory', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=300)),
                ('mainimage', models.ImageField(blank=True, upload_to='products')),
                ('preview_text', models.TextField(max_length=200, verbose_name='Preview Text')),
                ('detail_text', models.TextField(max_length=1000, verbose_name='Detail Text')),
                ('price', models.DecimalField(decimal_places=2, default=10.0, max_digits=5)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Category')),
            ],
        ),
        migrations.DeleteModel(
            name='Kit',
        ),
        migrations.DeleteModel(
            name='VIPSlot',
        ),
    ]
