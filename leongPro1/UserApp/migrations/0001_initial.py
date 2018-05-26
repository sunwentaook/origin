# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=60)),
                ('uemail', models.CharField(max_length=40)),
                ('uaddree', models.CharField(max_length=100, null=True)),
                ('uphone', models.CharField(max_length=11, null=True)),
                ('ureceive', models.CharField(max_length=20, null=True)),
                ('uzip_code', models.CharField(max_length=6, null=True)),
            ],
        ),
    ]
