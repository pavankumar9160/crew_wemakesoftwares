# Generated by Django 5.1.2 on 2024-11-27 05:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_callbackrequest_contact_number_callbackrequest_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('geolocation', models.CharField(blank=True, max_length=255, null=True)),
                ('device', models.TextField()),
                ('browser', models.CharField(max_length=255)),
                ('screen_size', models.CharField(max_length=100)),
                ('network_type', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_information', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]