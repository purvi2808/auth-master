# Generated by Django 2.1.3 on 2019-05-04 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20190504_2011'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='task',
        ),
    ]
