# Generated by Django 2.0.5 on 2018-09-23 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20180923_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='/static/default_book.gif', upload_to=''),
        ),
    ]
