# Generated by Django 5.1 on 2024-10-09 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('katas', '0008_kata_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kata',
            old_name='nameKata',
            new_name='namekata',
        ),
    ]
