# Generated by Django 3.0.2 on 2020-04-23 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arogyasetu', '0002_login_register_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='register',
        ),
        migrations.AddField(
            model_name='test',
            name='mobile',
            field=models.IntegerField(null=True),
        ),
    ]
