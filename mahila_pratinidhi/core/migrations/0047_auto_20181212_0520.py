# Generated by Django 2.0.7 on 2018-12-12 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0046_auto_20181212_0426'),
    ]

    operations = [
        migrations.AddField(
            model_name='pratinidhishava',
            name='age_en',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='उमेर'),
        ),
        migrations.AddField(
            model_name='pratinidhishava',
            name='age_ne_NP',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='उमेर'),
        ),
        migrations.AddField(
            model_name='provincemahilapratinidhiform',
            name='age_en',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='उमेर'),
        ),
        migrations.AddField(
            model_name='provincemahilapratinidhiform',
            name='age_ne_NP',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='उमेर'),
        ),
        migrations.AddField(
            model_name='rastriyashava',
            name='age_en',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='उमेर'),
        ),
        migrations.AddField(
            model_name='rastriyashava',
            name='age_ne_NP',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='उमेर'),
        ),
    ]
