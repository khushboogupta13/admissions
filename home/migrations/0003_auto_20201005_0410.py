# Generated by Django 3.1 on 2020-10-05 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ip',
            name='ip',
            field=models.CharField(max_length=30),
        ),
    ]
