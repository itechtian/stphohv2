# Generated by Django 3.0.7 on 2021-01-19 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STPHOHapp2', '0002_auto_20210119_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectname', models.CharField(max_length=225)),
                ('thedate', models.CharField(max_length=100)),
                ('projectime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]