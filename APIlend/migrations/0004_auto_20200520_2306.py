# Generated by Django 3.0.4 on 2020-05-20 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIlend', '0003_auto_20200520_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debtitem',
            name='isActive',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='debtmonetary',
            name='isActive',
            field=models.BooleanField(default=False),
        ),
    ]
