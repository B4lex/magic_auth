# Generated by Django 3.1.6 on 2021-02-09 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magic_auth', '0003_auto_20210209_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='magicuser',
            name='login_count',
        ),
        migrations.AlterField(
            model_name='magicuser',
            name='email',
            field=models.EmailField(error_messages={'unique': 'User with specified email exists.'}, max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='magicuser',
            name='logins',
            field=models.ManyToManyField(to='magic_auth.LoginActivity'),
        ),
    ]
