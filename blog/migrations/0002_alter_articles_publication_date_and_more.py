# Generated by Django 4.1.2 on 2022-10-27 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='publication_date',
            field=models.DateTimeField(verbose_name='published'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='publication_date',
            field=models.DateTimeField(verbose_name='published'),
        ),
    ]
