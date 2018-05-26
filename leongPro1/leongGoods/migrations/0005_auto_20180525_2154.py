# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('leongGoods', '0004_auto_20180521_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dingdan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('uname', models.CharField(max_length=40)),
                ('utitle', models.CharField(max_length=40)),
                ('unumber', models.IntegerField()),
                ('ushu', models.IntegerField()),
                ('uprice', models.DecimalField(max_digits=5, decimal_places=2)),
                ('udanjia', models.DecimalField(max_digits=5, decimal_places=2)),
                ('upic', ckeditor_uploader.fields.RichTextUploadingField()),
                ('dingdan', models.IntegerField()),
                ('zongjia', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Gouwu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('uname', models.CharField(max_length=40)),
                ('utitle', models.CharField(max_length=40)),
                ('unumber', models.IntegerField()),
                ('ushu', models.IntegerField()),
                ('uprice', models.DecimalField(max_digits=5, decimal_places=2)),
                ('udanjia', models.DecimalField(max_digits=5, decimal_places=2)),
                ('upic', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
        migrations.CreateModel(
            name='XD',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=40)),
                ('danhao', models.IntegerField()),
                ('zongjia', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gpub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 5, 25, 21, 54, 57, 670720), null=True),
        ),
    ]
