# Generated by Django 4.2.4 on 2023-09-25 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0053_alter_calendariomensal_dias_uteis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auxiliarcalculo',
            name='total_meses_horasprodutivas',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=10),
        ),
    ]
