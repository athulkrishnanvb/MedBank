# Generated by Django 5.0.6 on 2024-06-22 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0004_medicalproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blooddonation',
            name='master',
        ),
        migrations.RemoveField(
            model_name='medicalproduct',
            name='master',
        ),
        migrations.RemoveField(
            model_name='bloodrequest',
            name='master',
        ),
        migrations.DeleteModel(
            name='Master',
        ),
    ]
