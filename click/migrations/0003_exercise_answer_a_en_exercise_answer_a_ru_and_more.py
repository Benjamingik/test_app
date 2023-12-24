# Generated by Django 5.0 on 2023-12-11 14:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('click', '0002_rename_date_complated_result_date_completed_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='answer_a_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='answer_a_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='answer_a_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='answer_b_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='answer_b_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='answer_b_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='answer_c_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='answer_c_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='answer_c_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='answer_d_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='answer_d_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='answer_d_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='text_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='text_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='text_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='topic_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='click.topic'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='topic_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='click.topic'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='topic_uz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='click.topic'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='variant_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='click.variant'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='variant_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='click.variant'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='variant_uz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='click.variant'),
        ),
        migrations.AddField(
            model_name='result',
            name='user_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='results', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='result',
            name='user_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='results', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='result',
            name='user_uz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='results', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='result',
            name='variant_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='results', to='click.variant'),
        ),
        migrations.AddField(
            model_name='result',
            name='variant_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='results', to='click.variant'),
        ),
        migrations.AddField(
            model_name='result',
            name='variant_uz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='results', to='click.variant'),
        ),
        migrations.AddField(
            model_name='subject',
            name='name_en',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='name_ru',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='name_uz',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='name_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='name_ru',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='name_uz',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='subject_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='click.subject'),
        ),
        migrations.AddField(
            model_name='topic',
            name='subject_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='click.subject'),
        ),
        migrations.AddField(
            model_name='topic',
            name='subject_uz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='click.subject'),
        ),
        migrations.AddField(
            model_name='variant',
            name='subject_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='click.subject'),
        ),
        migrations.AddField(
            model_name='variant',
            name='subject_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='click.subject'),
        ),
        migrations.AddField(
            model_name='variant',
            name='subject_uz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='click.subject'),
        ),
    ]
