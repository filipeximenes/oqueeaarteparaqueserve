# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whatisitfor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='what',
            name='art_is',
            field=models.TextField(max_length=b'140'),
        ),
    ]
