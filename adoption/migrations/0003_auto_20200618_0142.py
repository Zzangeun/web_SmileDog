# Generated by Django 3.0.7 on 2020-06-17 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoption', '0002_auto_20200617_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoption_post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='adoption/%Y/%m/%d'),
        ),
    ]