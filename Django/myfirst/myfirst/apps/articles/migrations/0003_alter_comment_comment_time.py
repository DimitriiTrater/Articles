# Generated by Django 3.2.8 on 2021-10-18 20:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20211019_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_time',
            field=models.DateTimeField(verbose_name=datetime.datetime),
        ),
    ]
