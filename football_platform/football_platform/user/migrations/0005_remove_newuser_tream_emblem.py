# Generated by Django 4.1.2 on 2022-11-10 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0004_remove_newuser_coa_newuser_tream_emblem_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="newuser", name="tream_emblem",),
    ]
