# Generated by Django 4.2.7 on 2023-11-02 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_lancamento', models.DateTimeField(auto_created=True, blank=True)),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('ataque', models.IntegerField(blank=True, null=True)),
                ('vida', models.IntegerField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='campeoes')),
            ],
            options={
                'ordering': ['-data_lancamento'],
            },
        ),
        migrations.CreateModel(
            name='Custo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custo', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Habilidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='habilidades')),
                ('carta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='habilidades', to='war.carta')),
                ('custo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='war.custo')),
            ],
        ),
        migrations.CreateModel(
            name='Feitico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(upload_to='feiticos')),
                ('tipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feitiços', to='war.tipo')),
            ],
        ),
        migrations.AddField(
            model_name='carta',
            name='tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='war.tipo'),
        ),
    ]
