# Generated by Django 3.0.5 on 2020-04-12 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nickname', '0003_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='num',
            field=models.IntegerField(default=0),
        ),
    ]
