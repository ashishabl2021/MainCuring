# Generated by Django 4.2.5 on 2023-09-14 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curingapp', '0003_alter_schedule_curing_image_of_curing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='structural_element',
            name='Time_Bet_TwoCuring',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]