# Generated by Django 2.1 on 2018-11-23 08:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applyleave', '0012_auto_20181123_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveapplication',
            name='applied_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 23, 13, 52, 30, 205104), null=True),
        ),
    ]
