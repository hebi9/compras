# Generated by Django 4.0 on 2023-12-13 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppCompras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallelista',
            name='lista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='AppCompras.listas'),
        ),
    ]