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
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 5, 21, 11, 21, 48, 651556)),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gpubj_date',
            field=models.DateTimeField(null=True),
        ),
    ]
