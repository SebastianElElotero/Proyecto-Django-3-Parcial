# Generated by Django 5.1.2 on 2024-10-24 21:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestion_pedidos', '0001_initial'),
        ('gestion_usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('metodo_pago', models.CharField(choices=[('T', 'Tarjeta de Crédito'), ('P', 'PayPal'), ('D', 'Depósito Bancario')], max_length=1)),
                ('estado', models.CharField(choices=[('P', 'Pendiente'), ('C', 'Completado'), ('F', 'Fallido')], default='P', max_length=1)),
                ('fecha_pago', models.DateTimeField(auto_now_add=True)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_pedidos.pedido')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_usuarios.usuario')),
            ],
        ),
    ]