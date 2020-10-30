# Generated by Django 3.1.2 on 2020-10-30 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20201030_0430'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Mision',
                'verbose_name_plural': 'Mision',
            },
        ),
    ]
