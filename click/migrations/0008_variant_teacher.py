# Generated by Django 5.0 on 2023-12-15 15:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('click', '0007_remove_variant_user_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='variant',
            name='teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='click.teacher'),
        ),
    ]
