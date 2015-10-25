# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20151016_1649'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='html_text',
        ),
        migrations.AddField(
            model_name='post',
            name='markdown_text',
            field=models.TextField(default=''),
        ),
    ]
