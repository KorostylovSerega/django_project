# Generated by Django 4.1.2 on 2022-10-21 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookLibrary', '0002_books_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='genre',
            new_name='genres',
        ),
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]