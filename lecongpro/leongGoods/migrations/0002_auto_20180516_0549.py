# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('leongGoods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='gpub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 5, 16, 5, 49, 13, 912336)),
        ),
    ]
