# Generated by Django 5.1.1 on 2024-10-05 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='numbers_of_likes',
            field=models.IntegerField(default=0),
        ),
    ]
