# Generated by Django 3.0.7 on 2020-07-14 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('link', '0008_auto_20200713_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkdb',
            name='catalogChoice',
            field=models.CharField(choices=[('code', 'Code'), ('stock', 'Stock'), ('news', 'News'), ('shoping', 'Shoping'), ('books', 'Books'), ('sport', 'Sport'), ('games', 'Games'), ('videos', 'Videos'), ('music', 'Music'), ('work', 'Work')], default='code', max_length=20),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalogChoice', multiselectfield.db.fields.MultiSelectField(choices=[('code', 'Code'), ('stock', 'Stock'), ('news', 'News'), ('shoping', 'Shoping'), ('books', 'Books'), ('sport', 'Sport'), ('games', 'Games'), ('videos', 'Videos'), ('music', 'Music'), ('work', 'Work')], default='code', max_length=59)),
                ('img', models.ImageField(upload_to='link/static/images')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
