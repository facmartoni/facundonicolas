# Generated by Django 3.0.1 on 2019-12-28 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20191228_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(max_length=200, unique=True),
        ),
    ]