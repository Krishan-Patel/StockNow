# Generated by Django 3.1.4 on 2021-04-28 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='last_update',
        ),
    ]
