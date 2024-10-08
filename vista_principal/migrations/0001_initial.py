# Generated by Django 5.1 on 2024-08-21 03:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_orden', models.DateTimeField(auto_now_add=True)),
                ('completado', models.BooleanField(default=False)),
                ('id_transaccion', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('precio', models.FloatField()),
                ('ram', models.CharField(max_length=200, null=True)),
                ('almacenamiento', models.CharField(max_length=200, null=True)),
                ('cpu', models.CharField(max_length=200, null=True)),
                ('camara_trasera', models.CharField(max_length=200, null=True)),
                ('camara_frontal', models.CharField(max_length=200, null=True)),
                ('pantalla', models.CharField(max_length=200, null=True)),
                ('bateria', models.CharField(max_length=200, null=True)),
                ('android', models.CharField(max_length=200, null=True)),
                ('color', models.CharField(max_length=200, null=True)),
                ('cantidad', models.IntegerField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='datos_envio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('direccion', models.CharField(max_length=100, null=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vista_principal.cliente')),
                ('orden', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vista_principal.orden')),
            ],
        ),
        migrations.CreateModel(
            name='orden_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(blank=True, default=0, null=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('orden', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vista_principal.orden')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vista_principal.producto')),
            ],
        ),
    ]
