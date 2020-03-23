# Generated by Django 3.0.4 on 2020-03-23 20:21

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countrycode', models.CharField(choices=[('DE', 'Deutschland'), ('AT', 'Österreich')], default='DE', max_length=2)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('sonstige_infos', models.TextField(default='')),
                ('ansprechpartner', models.CharField(default='', max_length=100)),
                ('telefon', models.CharField(default='', max_length=100)),
                ('firmenname', models.CharField(default='', max_length=100)),
                ('plz', models.CharField(max_length=5, null=True)),
                ('uuid', models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True)),
                ('registration_date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
            ],
            options={
                'ordering': ['email'],
            },
        ),
    ]
