# Generated by Django 4.2.4 on 2023-09-02 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_rename_cargos_employee_cargo'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='custo_salario',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
