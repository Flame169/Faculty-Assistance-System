# Generated by Django 4.1.4 on 2023-02-05 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0013_announcements1_delete_announcements_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcements1',
            name='text',
            field=models.TextField(max_length=10000),
        ),
    ]
