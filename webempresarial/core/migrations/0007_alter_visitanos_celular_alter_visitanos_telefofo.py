# Generated by Django 4.0 on 2022-03-04 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_visitanos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitanos',
            name='celular',
            field=models.IntegerField(verbose_name='numero celular'),
        ),
        migrations.AlterField(
            model_name='visitanos',
            name='telefofo',
            field=models.IntegerField(verbose_name='numero de telefono'),
        ),
    ]
