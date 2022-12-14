# Generated by Django 4.1.2 on 2022-10-29 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tream", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FullEvents",
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
                ("team_id", models.CharField(max_length=64, verbose_name="团队ID")),
                (
                    "origin_player_id",
                    models.CharField(max_length=64, verbose_name="起始球员身份"),
                ),
                (
                    "destination_player_id",
                    models.CharField(max_length=64, null=True, verbose_name="目的球员身份"),
                ),
                (
                    "match_period",
                    models.IntegerField(
                        choices=[[0, "1H"], [1, "2H"]], verbose_name="比赛进行阶段"
                    ),
                ),
                ("event_time", models.FloatField(verbose_name="比赛时间")),
                ("event_type", models.CharField(max_length=64, verbose_name="事件类型")),
                (
                    "event_sub_type",
                    models.CharField(max_length=64, verbose_name="详细事件类型"),
                ),
                (
                    "event_origin_x",
                    models.IntegerField(default=0, verbose_name="起始球员位置X"),
                ),
                (
                    "event_origin_y",
                    models.IntegerField(default=0, verbose_name="起始球员位置Y"),
                ),
                (
                    "event_destination_x",
                    models.IntegerField(default=0, verbose_name="目的球员位置X"),
                ),
                (
                    "event_destination_y",
                    models.IntegerField(default=0, verbose_name="目的球员位置Y"),
                ),
                (
                    "match_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tream.match",
                        verbose_name="比赛ID",
                    ),
                ),
            ],
            options={"verbose_name_plural": "球员动作统计与分析", "db_table": "FullEvents",},
        ),
    ]
