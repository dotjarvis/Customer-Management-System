# Generated by Django 4.1.5 on 2023-01-19 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pis',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
