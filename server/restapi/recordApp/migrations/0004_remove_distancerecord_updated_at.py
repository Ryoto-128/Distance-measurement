# Generated by Django 3.1.5 on 2021-01-18 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recordApp', '0003_auto_20210118_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distancerecord',
            name='updated_at',
        ),
    ]
