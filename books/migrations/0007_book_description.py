# Generated by Django 4.1 on 2022-10-15 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_book_manga_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
