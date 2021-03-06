# Generated by Django 3.0.4 on 2020-04-04 03:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projecto',
            options={'ordering': ['-fch_creado']},
        ),
        migrations.AddField(
            model_name='projecto',
            name='titulo',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, verbose_name='titulo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projecto',
            name='fch_creado',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha Creación'),
        ),
        migrations.AlterField(
            model_name='projecto',
            name='fch_mod',
            field=models.DateField(auto_now=True, verbose_name='Fecha Creación'),
        ),
    ]
