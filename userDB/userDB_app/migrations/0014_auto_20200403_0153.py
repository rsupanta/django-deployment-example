# Generated by Django 3.0.4 on 2020-04-02 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userDB_app', '0013_delete_formdb'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='userDB',
        ),
    ]
