# Generated by Django 4.2.2 on 2023-08-04 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_articulo_publicado_alter_blogcomment_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='content',
            field=models.TextField(verbose_name='contenido'),
        ),
    ]
