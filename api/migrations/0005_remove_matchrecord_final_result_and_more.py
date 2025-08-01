# Generated by Django 5.2.3 on 2025-06-26 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_matchrecord_final_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matchrecord',
            name='final_result',
        ),
        migrations.AddField(
            model_name='matchrecord',
            name='guest_team_score',
            field=models.PositiveIntegerField(blank=True, help_text='Goals scored by the guest team', null=True),
        ),
        migrations.AddField(
            model_name='matchrecord',
            name='host_team_score',
            field=models.PositiveIntegerField(blank=True, help_text='Goals scored by the host team', null=True),
        ),
    ]
