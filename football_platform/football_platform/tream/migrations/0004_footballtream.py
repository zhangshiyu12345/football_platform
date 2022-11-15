# Generated by Django 4.1.2 on 2022-11-10 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tream", "0003_remove_passingevents_match_id_delete_fullevents_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="FootballTream",
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
                ("name", models.CharField(max_length=256, verbose_name="球队名称")),
                (
                    "tream_emblem",
                    models.ImageField(
                        default="default.jpg", upload_to="tream", verbose_name="球队队徽"
                    ),
                ),
            ],
            options={"verbose_name_plural": "球队", "db_table": "Tream",},
        ),
    ]
