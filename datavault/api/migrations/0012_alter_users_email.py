# Generated by Django 5.0 on 2023-12-17 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_files_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=50, unique=True, verbose_name='user_email'),
        ),
    ]
