# Generated by Django 4.0.6 on 2022-07-27 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_newuser_score'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newuser',
            old_name='body_weight',
            new_name='weight',
        ),
    ]