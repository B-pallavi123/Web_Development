# Generated by Django 5.0.7 on 2025-02-26 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_email_notification'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Email_Notification',
        ),
    ]
