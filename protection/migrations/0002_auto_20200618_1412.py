# Generated by Django 3.0.7 on 2020-06-18 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protection_post',
            name='protection_image',
            field=models.ImageField(blank=True, null=True, upload_to='protection/%Y/%m/%d'),
        ),
    ]