# Generated manually by Copilot on 2026-02-27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0005_remove_cliente_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='prazo_entrega',
            field=models.DateField(blank=True, null=True),
        ),
    ]
