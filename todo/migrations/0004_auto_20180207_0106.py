# Generated by Django 2.0 on 2018-02-06 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20180207_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='Done',
            field=models.BooleanField(default=False),
        ),
    ]
