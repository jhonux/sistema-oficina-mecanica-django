# Generated by Django 4.1.4 on 2023-06-08 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0002_remove_servico_protocole_servico_protocolo'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='identificador',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
    ]
