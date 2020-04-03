# Generated by Django 3.0.4 on 2020-04-03 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='border_value',
            field=models.FloatField(default=0.5, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='measurement',
            name='ip_feedback',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='value',
            field=models.FloatField(max_length=100),
        ),
    ]
