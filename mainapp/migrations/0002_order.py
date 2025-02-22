# Generated by Django 5.1.3 on 2025-02-05 21:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(help_text="The customer's name", max_length=100)),
                ('address', models.CharField(help_text='The delivery address', max_length=200)),
                ('card_number', models.CharField(help_text='Credit card number', max_length=16)),
                ('card_expiry_month', models.CharField(help_text='Card expiry month', max_length=2)),
                ('card_expiry_year', models.CharField(help_text='Card expiry year', max_length=4)),
                ('card_cvv', models.CharField(help_text='Card CVV code', max_length=3)),
                ('order_date', models.DateTimeField(auto_now_add=True, help_text='Date and time when the order was placed')),
                ('pizza', models.ForeignKey(help_text='The pizza they ordered', on_delete=django.db.models.deletion.CASCADE, to='mainapp.pizza')),
                ('user', models.ForeignKey(help_text='The user who placed the order', on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
