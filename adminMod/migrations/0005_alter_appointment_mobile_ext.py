# Generated by Django 4.1.1 on 2022-10-07 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminMod', '0004_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='mobile_ext',
            field=models.CharField(max_length=3),
        ),
    ]
