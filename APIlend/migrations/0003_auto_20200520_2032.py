# Generated by Django 3.0.4 on 2020-05-20 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APIlend', '0002_auto_20200511_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debtitem',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='debtitem',
            name='info',
            field=models.CharField(blank=True, max_length=280, null=True),
        ),
        migrations.CreateModel(
            name='Proposition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isActive', models.BooleanField(default=True)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='APIlend.DebtItem')),
                ('monetary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='APIlend.DebtMonetary')),
                ('receiver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiveProposition', to='APIlend.UserProfile')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sendProposition', to='APIlend.UserProfile')),
            ],
        ),
    ]
