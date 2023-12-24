# Generated by Django 4.2.7 on 2023-12-10 05:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('click', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='date_complated',
            new_name='date_completed',
        ),
        migrations.AlterField(
            model_name='result',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='result',
            name='variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='click.variant'),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answers', to='click.exercise'),
        ),
    ]
