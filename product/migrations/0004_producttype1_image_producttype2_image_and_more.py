# Generated by Django 4.0.4 on 2022-04-30 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_producttype1_expire_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttype1',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='producttype2',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='producttype3',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]