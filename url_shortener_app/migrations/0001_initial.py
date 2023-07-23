# Generated by Django 4.2.3 on 2023-07-23 06:58

from django.db import migrations, models
import shortuuid.main


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_url', models.URLField(unique=True)),
                ('short_url', models.CharField(default=shortuuid.main.ShortUUID.random, unique=True)),
            ],
        ),
    ]