# Generated by Django 2.0.2 on 2018-06-12 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_test', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trueorfalsequestionanswerrecord',
            name='answer',
            field=models.NullBooleanField(default=None),
        ),
    ]