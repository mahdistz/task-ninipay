# Generated by Django 4.0.4 on 2022-04-30 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_producttype1_image_producttype2_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttype1',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='producttype2',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='producttype3',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
