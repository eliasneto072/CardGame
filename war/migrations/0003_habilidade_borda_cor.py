# Generated by Django 4.2.7 on 2023-11-02 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('war', '0002_alter_carta_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='habilidade',
            name='borda_cor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]