# Generated by Django 4.1 on 2022-08-24 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_alter_customer_age_alter_customer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='pin',
            field=models.IntegerField(),
        ),
    ]
