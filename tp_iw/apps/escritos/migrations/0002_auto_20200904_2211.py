# Generated by Django 3.1 on 2020-09-05 01:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escritos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escrito',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 4, 22, 11, 18, 757307)),
        ),
    ]