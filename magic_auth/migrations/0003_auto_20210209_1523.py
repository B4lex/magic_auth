# Generated by Django 3.1.6 on 2021-02-09 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magic_auth', '0002_auto_20210209_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magicuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]