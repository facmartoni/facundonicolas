# Generated by Django 3.0.1 on 2020-01-22 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_subscriber'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='ipv4',
            field=models.CharField(default='', max_length=15, verbose_name='IP'),
            preserve_default=False,
        ),
    ]