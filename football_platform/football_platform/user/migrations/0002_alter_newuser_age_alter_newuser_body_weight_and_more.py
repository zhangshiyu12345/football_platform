# Generated by Django 4.0.6 on 2022-07-26 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='age',
            field=models.IntegerField(null=True, verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='body_weight',
            field=models.FloatField(null=True, verbose_name='体重'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='position',
            field=models.IntegerField(choices=[[0, '前锋'], [1, '左边锋'], [2, '右边锋'], [3, '前腰'], [4, '中前卫'], [5, '中后卫'], [6, '左后卫'], [7, '右后卫'], [8, '门将']], null=True, verbose_name='位置'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='sex',
            field=models.IntegerField(choices=[[0, '女'], [1, '男']], null=True, verbose_name='性别'),
        ),
    ]
