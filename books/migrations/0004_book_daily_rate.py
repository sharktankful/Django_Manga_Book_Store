# Generated by Django 4.1 on 2022-10-10 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='daily_rate',
            field=models.FloatField(null=True),
        ),
    ]
