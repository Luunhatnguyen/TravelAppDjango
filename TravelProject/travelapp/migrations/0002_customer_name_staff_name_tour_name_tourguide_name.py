# Generated by Django 4.0.4 on 2022-05-21 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(default='thong tin', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='name',
            field=models.CharField(default='thong tin', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='name',
            field=models.CharField(default='thong tin', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tourguide',
            name='name',
            field=models.CharField(default='thong tin', max_length=255, null=True),
        ),
    ]