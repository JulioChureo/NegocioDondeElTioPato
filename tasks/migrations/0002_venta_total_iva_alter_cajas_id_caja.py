# Generated by Django 4.2.2 on 2023-07-09 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='total_iva',
            field=models.IntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='cajas',
            name='id_caja',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]