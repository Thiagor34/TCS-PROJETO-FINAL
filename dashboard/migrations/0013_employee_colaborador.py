# Generated by Django 4.2.4 on 2023-08-29 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_remove_employee_colaborador_alter_employee_cargo'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='colaborador',
            field=models.ForeignKey(default=111, on_delete=django.db.models.deletion.CASCADE, to='dashboard.colaboradores'),
            preserve_default=False,
        ),
    ]