# Generated by Django 4.2.6 on 2023-11-04 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_usuario_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=40)),
                ('color', models.CharField(max_length=20)),
                ('placa', models.CharField(max_length=30)),
                ('kilometraje', models.IntegerField()),
            ],
        ),
    ]
