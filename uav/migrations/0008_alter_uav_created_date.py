# Generated by Django 4.1.7 on 2023-02-27 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uav', '0007_uav_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uav',
            name='created_date',
            field=models.DateTimeField(),
        ),
    ]
