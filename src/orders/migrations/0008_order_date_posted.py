# Generated by Django 2.1.5 on 2019-07-27 16:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20190723_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
