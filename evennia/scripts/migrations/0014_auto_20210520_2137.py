# Generated by Django 3.2.3 on 2021-05-20 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scripts", "0013_auto_20191025_0831"),
    ]

    operations = [
        migrations.AlterField(
            model_name="scriptdb",
            name="db_interval",
            field=models.IntegerField(
                default=-1,
                help_text="how often to repeat script, in seconds. <= 0 means off.",
                verbose_name="interval",
            ),
        ),
        migrations.AlterField(
            model_name="scriptdb",
            name="db_persistent",
            field=models.BooleanField(default=True, verbose_name="survive server reboot"),
        ),
    ]
