# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0004_auto_20160614_0946'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdevice',
            old_name='device_id',
            new_name='device_name',
        ),
        migrations.RenameField(
            model_name='userdevice',
            old_name='user_id',
            new_name='user_name',
        ),
        migrations.RemoveField(
            model_name='mobiledetail',
            name='device_id',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='user_id',
        ),
    ]
