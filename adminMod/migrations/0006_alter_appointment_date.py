# Generated by Django 4.1.1 on 2022-10-09 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminMod', '0005_alter_appointment_mobile_ext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(max_length=50),
        ),
    ]
