# Generated by Django 3.0.6 on 2020-05-20 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('framework', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='mobile',
            field=models.BigIntegerField(default=0),
        ),
    ]
