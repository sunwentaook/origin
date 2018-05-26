# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('leongGoods', '0003_auto_20180521_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='gpub_date',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 5, 21, 11, 28, 20, 491087)),
        ),
    ]
