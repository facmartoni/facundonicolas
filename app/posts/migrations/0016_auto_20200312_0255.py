# Generated by Django 3.0.3 on 2020-03-12 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_subscriber_ipv4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(null=True, upload_to='static/posts/covers', verbose_name='Cover'),
        ),
    ]