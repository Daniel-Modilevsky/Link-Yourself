# Generated by Django 3.0.7 on 2020-07-18 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('link', '0014_auto_20200718_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkdb',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
