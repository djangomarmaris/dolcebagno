# Generated by Django 4.0.5 on 2023-03-17 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_rename_nodropdown_product_bestsale_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%y/%m/%d', verbose_name='(250x250)'),
        ),
    ]
