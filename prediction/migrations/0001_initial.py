# Generated by Django 4.0.4 on 2022-06-01 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Historics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique='TRUE')),
                ('symptom_n1', models.CharField(max_length=100)),
                ('symptom_n2', models.CharField(max_length=100)),
                ('symptom_n3', models.CharField(max_length=100)),
                ('prediction', models.CharField(max_length=100)),
            ],
        ),
    ]
