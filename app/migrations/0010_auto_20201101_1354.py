# Generated by Django 3.1.2 on 2020-11-01 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_mision_vision'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insumo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='insumo'),
        ),
    ]