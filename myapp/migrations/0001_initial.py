# Generated by Django 5.1.2 on 2024-11-14 07:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=15)),
                ('alternate_contact_number', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('aadhar_card_front', models.ImageField(blank=True, null=True, upload_to='profiles/')),
                ('aadhar_card_back', models.ImageField(blank=True, null=True, upload_to='profiles/')),
                ('pan_card', models.ImageField(blank=True, null=True, upload_to='profiles/')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profiles/')),
                ('occupation', models.IntegerField(choices=[(0, 'select'), (1, 'Student'), (2, 'Salaried'), (3, 'Self-Employeed'), (4, 'Others')], default=0)),
                ('course_name', models.CharField(blank=True, max_length=500, null=True)),
                ('college_name', models.CharField(blank=True, max_length=500, null=True)),
                ('company_name', models.CharField(blank=True, max_length=500, null=True)),
                ('dc_code', models.CharField(blank=True, max_length=20, null=True)),
                ('ip_address', models.CharField(blank=True, max_length=500, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_csa', models.BooleanField(default=False, null=True)),
                ('is_logged_in', models.BooleanField(default=False)),
                ('is_idle', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
