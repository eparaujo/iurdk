# Generated by Django 5.1 on 2024-09-27 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karatestyles', '0002_remove_karatestyle_gran_master_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='karatestyle',
            name='bases',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='karatestyle',
            name='origin_style',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='karatestyle',
            name='qtde_katas',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
