# Generated by Django 2.0.5 on 2018-09-23 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.URLField(default='/static/deafult_book.gif'),
        ),
    ]
