# Generated by Django 4.1.5 on 2023-01-19 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_customer_profile_pis'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='profile_pis',
            new_name='profile_pic',
        ),
    ]
