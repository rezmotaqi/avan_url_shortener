# Generated by Django 4.2.3 on 2023-07-23 08:54

from django.db import migrations, models
import shortuuid.main


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener_app', '0002_alter_url_short_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.CharField(default=shortuuid.main.ShortUUID.random, unique=True),
        ),
    ]
