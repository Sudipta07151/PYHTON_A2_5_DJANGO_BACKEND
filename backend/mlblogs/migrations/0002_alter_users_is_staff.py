# Generated by Django 4.0 on 2022-01-02 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlblogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
