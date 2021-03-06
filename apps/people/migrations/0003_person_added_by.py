# Generated by Django 3.2.12 on 2022-02-25 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('people', '0002_auto_20220218_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='added_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='people_added_by', to='auth.user', verbose_name='Added by'),
            preserve_default=False,
        ),
    ]
