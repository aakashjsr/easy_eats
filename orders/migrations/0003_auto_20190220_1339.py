# Generated by Django 2.1.7 on 2019-02-20 13:39

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0002_auto_20190214_0833'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cancelled_by',
            field=models.ForeignKey(
                default='',
                on_delete=django.db.models.deletion.CASCADE,
                related_name='orders_cancelled',
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='restaurant_rating',
            field=models.SmallIntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MaxValueValidator(5),
                    django.core.validators.MinValueValidator(1),
                ],
            ),
        ),
        migrations.AlterField(
            model_name='order',
            name='restaurant_timing_rating',
            field=models.SmallIntegerField(
                blank=True,
                choices=[
                    (0, 'Early by 5 mins'),
                    (1, 'Early by more than 10 mins'),
                    (2, 'On Time'),
                    (3, 'Late by 5 mins'),
                    (4, 'Late by more than 10 mins'),
                ],
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(
                choices=[
                    ('ACTIVE', 'ACTIVE'),
                    ('BOOKED', 'BOOKED'),
                    ('COMPLETED', 'COMPLETED'),
                    ('CANCELLED', 'CANCELLED'),
                ],
                default='BOOKED',
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name='order',
            name='user_rating',
            field=models.PositiveIntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MaxValueValidator(5),
                    django.core.validators.MinValueValidator(1),
                ],
            ),
        ),
    ]