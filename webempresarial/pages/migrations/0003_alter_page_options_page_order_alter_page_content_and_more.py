# Generated by Django 4.0 on 2022-02-05 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_page_options_alter_page_content_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['order', 'title'], 'verbose_name': 'pagina', 'verbose_name_plural': 'paginas'},
        ),
        migrations.AddField(
            model_name='page',
            name='order',
            field=models.SmallIntegerField(default=0, verbose_name='orden de las paginas'),
        ),
        migrations.AlterField(
            model_name='page',
            name='content',
            field=models.TextField(verbose_name='contenido'),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=100, verbose_name='titulo'),
        ),
    ]
