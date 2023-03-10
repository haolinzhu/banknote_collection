# Generated by Django 3.1.7 on 2023-02-18 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banknotes', '0003_auto_20230213_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banknote',
            name='day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='banknote',
            name='intro_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='banknote',
            name='intro_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='banknote',
            name='intro_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='banknote',
            name='month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='banknote',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
