# Generated by Django 2.0.2 on 2018-05-03 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_test', '0006_auto_20180503_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='choicequestion',
            name='test_used',
            field=models.ManyToManyField(blank=True, null=True, to='online_test.Test'),
        ),
        migrations.AddField(
            model_name='trueorfalsequestion',
            name='test_used',
            field=models.ManyToManyField(blank=True, null=True, to='online_test.Test'),
        ),
    ]
