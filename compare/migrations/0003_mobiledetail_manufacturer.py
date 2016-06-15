# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0002_auto_20160614_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobiledetail',
            name='manufacturer',
            field=models.CharField(default=b'Samsung', max_length=50),
            preserve_default=True,
        ),
    ]
