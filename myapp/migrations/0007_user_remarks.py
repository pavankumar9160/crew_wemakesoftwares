# Generated by Django 5.1.2 on 2024-11-26 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_delete_deviceinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='remarks',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
