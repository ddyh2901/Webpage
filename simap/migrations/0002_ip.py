# Generated by Django 2.2.dev20180718181542 on 2018-08-01 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IP', models.CharField(max_length=50)),
            ],
        ),
    ]