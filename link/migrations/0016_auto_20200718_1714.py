# Generated by Django 3.0.7 on 2020-07-18 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0015_auto_20200718_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linkdb',
            name='dateCreated',
        ),
        migrations.RemoveField(
            model_name='linkdb',
            name='dateLastSeen',
        ),
    ]