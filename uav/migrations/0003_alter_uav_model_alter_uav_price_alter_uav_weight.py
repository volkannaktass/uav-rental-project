# Generated by Django 4.1.7 on 2023-02-25 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uav', '0002_alter_uav_model_alter_uav_price_alter_uav_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uav',
            name='model',
            field=models.IntegerField(max_length=4),
        ),
        migrations.AlterField(
            model_name='uav',
            name='price',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='uav',
            name='weight',
            field=models.IntegerField(max_length=20),
        ),
    ]
