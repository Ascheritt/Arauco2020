# Generated by Django 2.1.8 on 2019-09-06 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balance_scorecard', '0013_info_kpi_observacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicador',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]