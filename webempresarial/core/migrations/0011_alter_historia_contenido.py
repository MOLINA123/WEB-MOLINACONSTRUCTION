# Generated by Django 4.0 on 2022-03-15 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_historia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historia',
            name='contenido',
            field=models.TextField(verbose_name='historia'),
        ),
    ]