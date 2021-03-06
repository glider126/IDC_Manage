# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-25 13:37
from __future__ import unicode_literals

import dc_user.utils
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='邮件地址')),
                ('head_img', models.ImageField(blank=True, default='head/user.jpg', null=True, storage=dc_user.utils.ImageStorage(), upload_to='head/%Y/%m/%d', verbose_name='头像')),
                ('name', models.CharField(max_length=64, verbose_name='姓名')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='加入日期')),
                ('first_ip', models.GenericIPAddressField(blank=True, null=True, protocol='IPV4', verbose_name='上次登录IP地址')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
