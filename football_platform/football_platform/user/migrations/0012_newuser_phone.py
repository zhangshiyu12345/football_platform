# Generated by Django 4.0.6 on 2022-09-08 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_newuser_body_newuser_control_newuser_defend_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='phone',
            field=models.CharField(default=1, max_length=11, verbose_name='手机'),
            preserve_default=False,
        ),
    ]
