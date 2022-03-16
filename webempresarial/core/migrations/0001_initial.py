# Generated by Django 4.0 on 2022-01-22 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeModelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('subtitle', models.CharField(max_length=100, verbose_name='Subtitilo')),
                ('image', models.ImageField(blank=True, null=True, upload_to='inicio', verbose_name='Imagen')),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': 'homemodelo',
                'verbose_name_plural': 'homemodelos',
            },
        ),
    ]
