# Generated by Django 5.0.6 on 2024-06-29 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0009_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]