# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MobileDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device_name', models.CharField(default=b'', max_length=50, verbose_name=b'Device Name')),
                ('device_id', models.PositiveIntegerField(default=0, verbose_name=b'id')),
                ('device_url', models.CharField(default=b'', max_length=50, verbose_name=b'Device Url')),
                ('source_website', models.CharField(default=b'', max_length=50, verbose_name=b'Website')),
                ('price', models.FloatField(verbose_name=b'Current Price')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='Userdetails',
            new_name='UserDetail',
        ),
        migrations.RemoveField(
            model_name='websitedetails',
            name='device_id',
        ),
        migrations.DeleteModel(
            name='Websitedetails',
        ),
        migrations.RemoveField(
            model_name='userdevice',
            name='Price_range',
        ),
        migrations.AddField(
            model_name='userdevice',
            name='minimum_price',
            field=models.FloatField(default=0, verbose_name=b'Price range'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userdevice',
            name='device_id',
            field=models.ForeignKey(to='compare.MobileDetail'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='MobileDetails',
        ),
    ]
