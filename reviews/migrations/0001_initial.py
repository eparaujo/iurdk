# Generated by Django 5.1 on 2024-09-04 19:43

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('katas', '0006_alter_kata_style'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Não é permitida avaliação inferior a ZERO!'), django.core.validators.MaxValueValidator(5, 'Não é permitida avaliação superior a CINCO!')])),
                ('comment', models.TextField(blank=True, null=True)),
                ('kata', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='katas', to='katas.kata')),
            ],
        ),
    ]
