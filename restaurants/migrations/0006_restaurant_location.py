# Generated by Django 2.1.7 on 2019-02-23 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190223_0900'),
        ('restaurants', '0005_auto_20190223_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurants', to='core.Location'),
        ),
    ]