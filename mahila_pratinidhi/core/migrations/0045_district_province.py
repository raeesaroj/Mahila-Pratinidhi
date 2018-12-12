# Generated by Django 2.0.7 on 2018-12-10 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_news_image_credit'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='districts', to='core.Province', verbose_name='प्रदेश'),
        ),
    ]