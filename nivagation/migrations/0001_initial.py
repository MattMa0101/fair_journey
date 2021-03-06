# Generated by Django 2.0.7 on 2018-08-30 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='road_construction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rwe_type', models.TextField(max_length=50, null=True)),
                ('rwe_status', models.TextField(max_length=50, null=True)),
                ('rwe_start_dt', models.TextField(max_length=50, null=True)),
                ('rwe_end_dt', models.TextField(max_length=50, null=True)),
                ('rwe_publish_text', models.TextField(max_length=500, null=True)),
                ('subject_pref_rdname', models.TextField(max_length=50, null=True)),
                ('traffic_delay', models.TextField(max_length=200, null=True)),
                ('speed_limit', models.TextField(max_length=50, null=True)),
                ('lanes_affected', models.TextField(max_length=50, null=True)),
            ],
        ),
    ]
