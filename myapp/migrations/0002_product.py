# Generated by Django 5.0.7 on 2024-07-24 10:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Kids', 'Kids')], max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.PositiveIntegerField()),
                ('product_desc', models.TextField()),
                ('product_image', models.ImageField(upload_to='product_images/')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
