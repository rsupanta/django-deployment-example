# Generated by Django 3.0.4 on 2020-03-30 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userDB_app', '0010_auto_20200329_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, default='gallery/img.jpeg', upload_to='gallery'),
        ),
    ]