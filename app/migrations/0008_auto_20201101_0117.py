# Generated by Django 3.1.2 on 2020-11-01 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20201101_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeria',
            name='imagen',
            field=models.ImageField(null=True, upload_to='galeria'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='imagen',
            field=models.ImageField(null=True, upload_to='slider'),
        ),
    ]
