# Generated by Django 3.0.4 on 2020-03-28 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userDB_app', '0008_auto_20200329_0250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_img',
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='/gallery/img.jpeg', upload_to='gallery'),
        ),
    ]
