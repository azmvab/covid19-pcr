# Generated by Django 3.2.12 on 2022-02-18 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='collection_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='hesn_no',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AddField(
            model_name='person',
            name='report_no',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
    ]
