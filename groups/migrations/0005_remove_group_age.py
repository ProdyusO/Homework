# Generated by Django 3.2.4 on 2021-06-09 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_group_birthday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='age',
        ),
    ]