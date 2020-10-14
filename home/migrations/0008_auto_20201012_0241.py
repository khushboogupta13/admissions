# Generated by Django 3.1 on 2020-10-12 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_demo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demo',
            name='region',
            field=models.CharField(blank=True, db_column='REGION', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='demo',
            name='state',
            field=models.CharField(blank=True, db_column='STATE', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='mopup',
            name='region',
            field=models.CharField(blank=True, db_column='REGION', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='mopup',
            name='state',
            field=models.CharField(blank=True, db_column='STATE', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='round1',
            name='region',
            field=models.CharField(blank=True, db_column='REGION', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='round1',
            name='state',
            field=models.CharField(blank=True, db_column='STATE', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='round2',
            name='region',
            field=models.CharField(blank=True, db_column='REGION', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='round2',
            name='state',
            field=models.CharField(blank=True, db_column='STATE', max_length=25, null=True),
        ),
    ]