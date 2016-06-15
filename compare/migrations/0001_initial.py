# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MobileDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device_name', models.CharField(default=b'', max_length=50, verbose_name=b'Device Name')),
                ('device_id', models.PositiveIntegerField(default=0, verbose_name=b'id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Userdetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(default=b'', max_length=50, verbose_name=b'User Name')),
                ('user_id', models.PositiveIntegerField(default=0, verbose_name=b'user id')),
                ('user_email', models.CharField(max_length=50, verbose_name=b'user email')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Userdevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Price_range', models.FloatField(verbose_name=b'Price range')),
                ('device_id', models.ForeignKey(to='compare.MobileDetails')),
                ('user_id', models.ForeignKey(to='compare.Userdetails')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Websitedetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Wname', models.CharField(default=b'', max_length=50, verbose_name=b'Website')),
                ('wid', models.PositiveIntegerField(default=0, verbose_name=b'user id')),
                ('wurl', models.CharField(max_length=50, verbose_name=b'user email')),
                ('lprice', models.FloatField(verbose_name=b'Price')),
                ('device_id', models.ForeignKey(to='compare.MobileDetails')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
