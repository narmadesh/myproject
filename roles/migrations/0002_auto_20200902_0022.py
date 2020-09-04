# Generated by Django 3.1.1 on 2020-09-01 18:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave_Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(default=datetime.date.today)),
                ('description', models.TextField()),
                ('leave_avail', models.IntegerField()),
                ('applied_on', models.DateField(default=datetime.date.today)),
                ('approved_on', models.DateField(default=datetime.date.today)),
                ('approved_by', models.CharField(max_length=50)),
                ('status', models.CharField(default='Pending', max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='created_at',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='users',
            name='status',
            field=models.CharField(default='Enabled', max_length=25),
        ),
    ]