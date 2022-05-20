# Generated by Django 4.0.1 on 2022-05-19 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0003_blocks'),
    ]

    operations = [
        migrations.AddField(
            model_name='blocks',
            name='log_index',
            field=models.IntegerField(default=False),
        ),
        migrations.AddField(
            model_name='blocks',
            name='value',
            field=models.BigIntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='blocks',
            name='token_id',
            field=models.IntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='blocks',
            name='transaction_index',
            field=models.IntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='blocks',
            name='verified',
            field=models.IntegerField(default=False),
        ),
    ]
