# Generated by Django 4.1.2 on 2022-10-11 08:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0014_remove_newuser_code"),
    ]

    operations = [
        migrations.CreateModel(
            name="Notice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=256, verbose_name="通知标题")),
                ("content", models.TextField(verbose_name="内容")),
                ("author", models.CharField(max_length=64, verbose_name="作者")),
                (
                    "create_time",
                    models.DateTimeField(
                        default=datetime.datetime.now, verbose_name="创建时间"
                    ),
                ),
            ],
            options={"db_table": "Notice",},
        ),
    ]
