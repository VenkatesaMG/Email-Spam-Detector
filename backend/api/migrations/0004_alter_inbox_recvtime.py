# Generated by Django 5.1 on 2024-08-31 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_inbox_recvtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inbox',
            name='recvTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
