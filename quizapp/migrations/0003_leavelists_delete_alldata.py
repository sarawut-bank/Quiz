# Generated by Django 4.2.5 on 2023-09-21 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0002_alter_alldata_body_response_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leavelists',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('surename', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('type_leave', models.CharField(max_length=100)),
                ('cause', models.CharField(max_length=255)),
                ('date_first', models.DateField()),
                ('date_end', models.DateField()),
                ('date_save', models.DateTimeField()),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='AllData',
        ),
    ]