# Generated by Django 2.1.8 on 2019-09-06 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('balance_scorecard', '0006_auto_20190831_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acumulado_kpi',
            name='valor_kpi',
        ),
        migrations.AddField(
            model_name='acumulado_kpi',
            name='indicador',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to='balance_scorecard.Indicador'),
            preserve_default=False,
        ),
    ]