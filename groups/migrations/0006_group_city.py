# Generated by Django 3.2.4 on 2021-06-09 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_remove_group_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
