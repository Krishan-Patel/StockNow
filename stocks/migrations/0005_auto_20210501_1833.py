# Generated by Django 3.1.4 on 2021-05-01 22:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stocks', '0004_stock_last_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='favourites',
            field=models.ManyToManyField(blank=True, default=None, related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='stock',
            name='last_update',
            field=models.DateTimeField(),
        ),
    ]
