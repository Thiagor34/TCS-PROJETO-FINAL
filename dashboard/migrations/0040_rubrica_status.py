# Generated by Django 4.2.4 on 2023-09-17 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0039_rename_combistivel_rubrica_combustivel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rubrica',
            name='status',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
