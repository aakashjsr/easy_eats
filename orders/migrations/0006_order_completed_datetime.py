# Generated by Django 2.1.7 on 2019-03-13 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20190313_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='completed_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
