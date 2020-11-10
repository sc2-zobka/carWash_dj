# Generated by Django 3.1.2 on 2020-11-10 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_vision'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('opciones_consulta', models.IntegerField(choices=[[0, 'consulta'], [1, 'reclamo'], [2, 'sugerencia'], [3, 'felicitaciones']])),
                ('mensaje', models.TextField()),
                ('ofertas', models.BooleanField(help_text='Reciba nuestras ofertas                                              exclusivas!')),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contacto',
            },
        ),
        migrations.AlterField(
            model_name='mision',
            name='descripcion',
            field=models.TextField(blank=True, help_text='Escriba un mensaje para                                   mostrar en la seccion de Mision                                   del sitio web', max_length=200),
        ),
        migrations.AlterField(
            model_name='vision',
            name='descripcion',
            field=models.TextField(blank=True, help_text='Escriba un mensaje para                                   mostrar en la seccion de Vision                                   del sitio web', max_length=200),
        ),
    ]
