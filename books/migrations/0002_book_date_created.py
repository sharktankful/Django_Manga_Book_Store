# Generated by Django 4.1 on 2022-10-10 14:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 10, 14, 34, 31, 556326, tzinfo=datetime.timezone.utc)),
        ),
    ]
