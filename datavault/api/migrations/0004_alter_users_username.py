# Generated by Django 5.0 on 2023-12-15 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_user_name_users_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=128, unique=True, verbose_name='username'),
        ),
    ]
