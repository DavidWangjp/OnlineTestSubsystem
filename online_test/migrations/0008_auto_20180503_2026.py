# Generated by Django 2.0.2 on 2018-05-03 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_test', '0007_auto_20180503_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choicequestion',
            name='test_used',
        ),
        migrations.RemoveField(
            model_name='trueorfalsequestion',
            name='test_used',
        ),
    ]