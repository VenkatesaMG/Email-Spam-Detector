# Generated by Django 5.1 on 2024-09-07 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_sent_alter_inbox_content'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Email',
        ),
    ]
