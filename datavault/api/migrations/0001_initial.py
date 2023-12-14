# Generated by Django 5.0 on 2023-12-13 00:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_date', models.DateField(auto_now_add=True)),
                ('file_compressed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=128, verbose_name='username')),
                ('email', models.EmailField(max_length=50, verbose_name='user_email')),
                ('password', models.CharField(max_length=256, verbose_name='user_password')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created_on')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.CharField(max_length=256)),
                ('file_size', models.PositiveIntegerField(verbose_name='file size(in Bytes)')),
                ('file_id', models.ManyToManyField(to='api.fileinfo')),
            ],
        ),
        migrations.AddField(
            model_name='fileinfo',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.users'),
        ),
    ]
