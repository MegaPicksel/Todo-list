# Generated by Django 2.0 on 2018-02-07 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20180207_0106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='Due_by',
            new_name='Due',
        ),
    ]
