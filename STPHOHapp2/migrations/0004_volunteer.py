# Generated by Django 3.0.7 on 2021-01-27 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STPHOHapp2', '0003_allproject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=125)),
                ('lastname', models.CharField(max_length=125)),
                ('address', models.CharField(max_length=125)),
                ('Phonenumber', models.CharField(max_length=125)),
                ('gender', models.CharField(max_length=125)),
            ],
        ),
    ]