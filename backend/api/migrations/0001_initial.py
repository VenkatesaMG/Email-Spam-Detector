# Generated by Django 5.1 on 2024-08-21 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailAddr', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
        ),
    ]
