# Generated by Django 4.2.6 on 2023-11-03 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('email', models.EmailField(max_length=30)),
                ('peso', models.IntegerField()),
                ('TipoPoliza', models.CharField(max_length=30)),
            ],
        ),
    ]
