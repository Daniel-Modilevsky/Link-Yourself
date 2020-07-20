# Generated by Django 3.0.7 on 2020-07-13 18:01

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0007_remove_linkdb_catalogname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkdb',
            name='catalogChoice',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('code', 'Code'), ('stock', 'Stock'), ('news', 'News'), ('shoping', 'Shoping'), ('books', 'Books'), ('sport', 'Sport'), ('games', 'Games'), ('videos', 'Videos'), ('music', 'Music'), ('work', 'Work')], default='code', max_length=59),
        ),
    ]