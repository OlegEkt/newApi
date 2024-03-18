# Generated by Django 4.0 on 2024-02-15 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='название игры')),
                ('description', models.TextField(verbose_name='описание игры')),
                ('stage_number', models.PositiveIntegerField(verbose_name='номер этапа')),
                ('stage_end_date', models.DateField(verbose_name='дата окончания этапа')),
            ],
            options={
                'verbose_name': 'игра',
                'verbose_name_plural': 'игры',
                'db_table': 'game',
            },
        ),
        migrations.CreateModel(
            name='GameUser',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='имя')),
                ('stage_1', models.BooleanField(verbose_name='этап 1')),
                ('stage_2', models.BooleanField(verbose_name='этап 2')),
                ('game', models.ManyToManyField(related_name='game_user', to='api.Game', verbose_name='игры')),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'пользователи',
                'db_table': 'game_user',
            },
        ),
    ]
