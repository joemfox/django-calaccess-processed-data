# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 17:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calaccess_processed', '0017_auto_20170121_1613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ballotmeasurecontest',
            old_name='division_id',
            new_name='division',
        ),
        migrations.RenameField(
            model_name='ballotmeasurecontest',
            old_name='election_id',
            new_name='election',
        ),
        migrations.RenameField(
            model_name='candidacy',
            old_name='committee_id',
            new_name='committee',
        ),
        migrations.RenameField(
            model_name='candidacy',
            old_name='party_id',
            new_name='party',
        ),
        migrations.RenameField(
            model_name='candidacy',
            old_name='person_id',
            new_name='person',
        ),
        migrations.RenameField(
            model_name='candidacy',
            old_name='post_id',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='candidatecontest',
            old_name='division_id',
            new_name='division',
        ),
        migrations.RenameField(
            model_name='candidatecontest',
            old_name='election_id',
            new_name='election',
        ),
        migrations.RenameField(
            model_name='candidatecontest',
            old_name='party_id',
            new_name='party',
        ),
        migrations.RenameField(
            model_name='candidatecontest',
            old_name='runoff_for_contest_id',
            new_name='runoff_for_contest',
        ),
        migrations.RenameField(
            model_name='retentioncontest',
            old_name='membership_id',
            new_name='membership',
        ),
    ]
