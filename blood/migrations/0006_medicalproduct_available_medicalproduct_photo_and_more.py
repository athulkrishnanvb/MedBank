# Generated by Django 5.0.6 on 2024-06-23 14:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0005_remove_blooddonation_master_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalproduct',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='medicalproduct',
            name='photo',
            field=models.ImageField(default='med_photos/de', upload_to='med_photos/'),
        ),
        migrations.AddField(
            model_name='medicalproduct',
            name='posted_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]