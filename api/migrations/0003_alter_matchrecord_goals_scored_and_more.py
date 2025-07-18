# Generated by Django 5.2.3 on 2025-06-26 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_player_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchrecord',
            name='goals_scored',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='matchrecord',
            name='red_cards',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='matchrecord',
            name='yellow_cards',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
