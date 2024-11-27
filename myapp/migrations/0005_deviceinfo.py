# Generated by Django 5.1.2 on 2024-11-26 09:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_historycapturedimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=45)),
                ('user_agent', models.TextField()),
                ('browser_data', models.TextField()),
                ('screen_width', models.IntegerField()),
                ('screen_height', models.IntegerField()),
                ('screen_color_depth', models.IntegerField()),
                ('network_type', models.CharField(blank=True, max_length=100, null=True)),
                ('network_downlink', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('accuracy', models.FloatField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]