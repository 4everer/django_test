# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('blogengine', '0005_auto_20151115_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='site',
            field=models.ForeignKey(default='1', to='sites.Site'),
            preserve_default=False,
        ),
    ]
