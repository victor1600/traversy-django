# Generated by Django 3.0.2 on 2020-02-03 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20200203_0315'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='sqft',
            field=models.IntegerField(default=0),
        ),
    ]
