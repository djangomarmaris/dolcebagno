# Generated by Django 4.0.5 on 2023-04-30 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_rules'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%y/%m/%d', verbose_name='1200x1125'),
        ),
    ]
