# Generated by Django 2.0.5 on 2018-09-23 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_auto_20180923_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.TextField(default='/static/default_book.gif'),
        ),
    ]
