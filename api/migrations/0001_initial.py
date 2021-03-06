# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MFASupport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('documentation', models.URLField(null=True, blank=True)),
                ('sms', models.BooleanField(default=False)),
                ('phone_call', models.BooleanField(default=False)),
                ('email', models.BooleanField(default=False)),
                ('hardware_token', models.BooleanField(default=False)),
                ('software_implementation', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('website', models.URLField(null=True, blank=True)),
                ('logo', models.URLField(null=True, blank=True)),
                ('twitter_handle', models.CharField(default=b'', max_length=256)),
                ('mfa_support', models.OneToOneField(null=True, blank=True, to='api.MFASupport')),
            ],
        ),
    ]
