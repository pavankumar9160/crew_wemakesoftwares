# Generated by Django 5.1.2 on 2024-11-27 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_callbackrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='callbackrequest',
            name='contact_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='callbackrequest',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
