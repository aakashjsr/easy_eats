# Generated by Django 2.1.7 on 2019-03-01 17:11

import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('BOOKED', 'BOOKED'), ('COMPLETED', 'COMPLETED'), ('CANCELLED', 'CANCELLED')], default='BOOKED', max_length=20)),
                ('comment', models.TextField(blank=True)),
                ('order_type', models.CharField(choices=[('Takeaway', 'Takeaway'), ('Dine-In', 'Dine-In')], default='Takeaway', max_length=50)),
                ('seats', models.PositiveIntegerField(default=0)),
                ('scheduled_datetime', models.DateTimeField()),
                ('cancellation_charge', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('points_earned', models.PositiveIntegerField(default=0)),
                ('user_rating', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('restaurant_rating', models.SmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('restaurant_timing_rating', models.SmallIntegerField(blank=True, choices=[(0, 'Early by 5 mins'), (1, 'Early by more than 10 mins'), (2, 'On Time'), (3, 'Late by 5 mins'), (4, 'Late by more than 10 mins')], null=True)),
                ('user_review', models.TextField(blank=True, max_length=280, null=True)),
                ('restaurant_review', models.TextField(blank=True, max_length=280)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('quantity', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('comment', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
