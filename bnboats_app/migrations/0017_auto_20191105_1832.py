# Generated by Django 2.1.7 on 2019-11-05 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnboats_app', '0016_auto_20191105_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boatblockeddates',
            name='blocked_dates',
            field=models.CharField(blank=True, default='', max_length=5000, null=True),
        ),
    ]
