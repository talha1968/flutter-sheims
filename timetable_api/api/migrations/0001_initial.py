# Generated by Django 3.2.16 on 2022-12-11 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacherName', models.CharField(max_length=100)),
                ('courseName', models.CharField(max_length=100)),
                ('classRoom', models.CharField(max_length=100)),
                ('classtime', models.TimeField()),
                ('day', models.CharField(max_length=100)),
            ],
        ),
    ]
