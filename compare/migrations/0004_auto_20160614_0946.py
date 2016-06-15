# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0003_mobiledetail_manufacturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobiledetail',
            name='device_url',
            field=models.CharField(default=b'', max_length=500, verbose_name=b'Device Url'),
            preserve_default=True,
        ),
    ]
